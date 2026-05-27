"""Generated from Smithy shape ``com.amazonaws.ecs#KeyValuePair``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class KeyValuePair(TypedDict):
    name: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The name of the key-value pair. For environment variables, this is the name of the environment variable.</p>"""
    value: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p>The value of the key-value pair. For environment variables, this is the value of the environment variable.</p>"""
