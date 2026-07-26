"""Generated from Smithy shape ``com.amazonaws.sesv2#ConfigurationSetName``."""

from typing import TypeAlias

"""<p>The name of a configuration set.</p> <p> <i>Configuration sets</i> are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.</p>"""
ConfigurationSetName: TypeAlias = str
