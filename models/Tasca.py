# -*- coding: utf-8 -*-
# Crear classe amb Python
from odoo import models, fields, api


class Tasca(models.Model):
    _name = 'todo.task'  # Serveix per referir-nos a aquesta classe del model d'es d'un altre lloc (Obligatori)
    name = fields.Char('Descripció', required=True)  # Per indicar el tipus de dada, el que surt a la pàgina web i per obligar a omplir-ho
    isDone = fields.Boolean('Feta?')  # Per indicar si la tasca està feta o no
    isActive = fields.Boolean('Activa?', default=True)  # Per activar o desactivar una tasca i posem valor per defecte

    @api.one
    def do_toggle_done(self):
        self.isDone = not self.isDone
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('isDone', '=', True)])
        done_recs.write({'isActive': False})
        return True