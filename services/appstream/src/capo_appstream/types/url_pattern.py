"""Generated from Smithy shape ``com.amazonaws.appstream#UrlPattern``."""

from typing import TypeAlias

"""<p>A glob pattern using wildcards (* for zero or more characters, ? for exactly one character) to match URLs for redirection rules. Patterns do not include a protocol prefix; HTTPS is enforced automatically. Valid examples: *, *.example.com, github.com/myorg/*, api?.example.com Invalid examples: https://example.com (no protocol), empty string</p>"""
UrlPattern: TypeAlias = str
