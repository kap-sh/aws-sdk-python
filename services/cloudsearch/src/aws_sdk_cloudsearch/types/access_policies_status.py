"""Generated from Smithy shape ``com.amazonaws.cloudsearch#AccessPoliciesStatus``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_cloudsearch._protocol.xml import Element
from aws_sdk_cloudsearch.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cloudsearch.types.option_status
    import aws_sdk_cloudsearch.types.policy_document


class AccessPoliciesStatus(TypedDict):
    options: "aws_sdk_cloudsearch.types.policy_document.PolicyDocument"
    status: "aws_sdk_cloudsearch.types.option_status.OptionStatus"


# --- awsQuery ser/de ---
def serialize_query(
    value: AccessPoliciesStatus, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.Options", str(value["options"])))
    import aws_sdk_cloudsearch.types.option_status

    aws_sdk_cloudsearch.types.option_status.serialize_query(
        value["status"], pairs, f"{prefix}.Status"
    )


def deserialize_query(el: Element) -> AccessPoliciesStatus:
    out: AccessPoliciesStatus = {}  # type: ignore[typeddict-item]
    child_options = el.find("Options")
    if child_options is not None:
        out["options"] = str(child_options.text or "")
    else:
        raise DeserializationError("AccessPoliciesStatus.options required")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_cloudsearch.types.option_status

        out["status"] = aws_sdk_cloudsearch.types.option_status.deserialize_query(
            child_status
        )
    else:
        raise DeserializationError("AccessPoliciesStatus.status required")
    return out
