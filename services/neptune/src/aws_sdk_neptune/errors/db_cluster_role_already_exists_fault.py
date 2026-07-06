"""Generated from Smithy shape ``com.amazonaws.neptune#DBClusterRoleAlreadyExistsFault``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_neptune._protocol.xml import Element
from aws_sdk_neptune.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_neptune.types.exception_message


class DBClusterRoleAlreadyExistsFault_(TypedDict, closed=True):
    message: NotRequired["aws_sdk_neptune.types.exception_message.ExceptionMessage"]
    """<p>A message describing the details of the problem.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DBClusterRoleAlreadyExistsFault_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> DBClusterRoleAlreadyExistsFault_:
    out: DBClusterRoleAlreadyExistsFault_ = {}  # type: ignore[typeddict-item]
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class DBClusterRoleAlreadyExistsFault(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.neptune#DBClusterRoleAlreadyExistsFault``."""

    code: str | None = "DBClusterRoleAlreadyExistsFault"

    def __init__(self, data: DBClusterRoleAlreadyExistsFault_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="DBClusterRoleAlreadyExistsFault",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "DBClusterRoleAlreadyExistsFault":
        return cls(deserialize_query(el))
