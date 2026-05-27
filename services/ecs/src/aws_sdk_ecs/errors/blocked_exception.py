"""Generated from Smithy shape ``com.amazonaws.ecs#BlockedException``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_ecs.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ecs.types.string


class BlockedException_(TypedDict):
    message: NotRequired["aws_sdk_ecs.types.string.String"]
    """<p> Message that describes the cause of the exception.</p>"""


class BlockedException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ecs#BlockedException``."""

    code: str | None = "BlockedException"

    def __init__(self, data: BlockedException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="BlockedException",
        )
        self.data = data
