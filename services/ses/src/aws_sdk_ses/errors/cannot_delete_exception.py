"""Generated from Smithy shape ``com.amazonaws.ses#CannotDeleteException``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element
from aws_sdk_ses.errors import ServiceError

if TYPE_CHECKING:
    import aws_sdk_ses.types.error_message
    import aws_sdk_ses.types.rule_or_rule_set_name


class CannotDeleteException_(TypedDict, closed=True):
    name: NotRequired["aws_sdk_ses.types.rule_or_rule_set_name.RuleOrRuleSetName"]
    """<p>Indicates that a resource could not be deleted because no resource with the specified name exists.</p>"""
    message: NotRequired["aws_sdk_ses.types.error_message.ErrorMessage"]


# --- awsQuery ser/de ---
def serialize_query(
    value: CannotDeleteException_, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "name" in value:
        pairs.append((f"{prefix}.Name", str(value["name"])))
    if "message" in value:
        pairs.append((f"{prefix}.message", str(value["message"])))


def deserialize_query(el: Element) -> CannotDeleteException_:
    out: CannotDeleteException_ = {}  # type: ignore[typeddict-item]
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_message = el.find("message")
    if child_message is not None:
        out["message"] = str(child_message.text or "")
    return out


class CannotDeleteException(ServiceError):
    """Modeled error for Smithy shape ``com.amazonaws.ses#CannotDeleteException``."""

    code: str | None = "CannotDeleteException"

    def __init__(self, data: CannotDeleteException_):
        super().__init__(
            "client",
            is_throttling_error=False,
            is_retryable=False,
            code="CannotDeleteException",
        )
        self.data = data

    @classmethod
    def from_query(cls, el: Element) -> "CannotDeleteException":
        return cls(deserialize_query(el))
