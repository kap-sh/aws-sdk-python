"""Generated from Smithy shape ``com.amazonaws.pi#SanitizedString``."""

from typing import TypeAlias

"""A generic string type that forbids characters that could expose our service (or services downstream) to security risks around injections."""
SanitizedString: TypeAlias = str
