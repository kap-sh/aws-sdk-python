"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteDomainEntryResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.operation


class DeleteDomainEntryResult(TypedDict, closed=True):
    operation: NotRequired["capo_lightsail.types.operation.Operation"]
    """<p>An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteDomainEntryResult) -> dict:
    out: dict = {}
    if "operation" in value:
        import capo_lightsail.types.operation

        out["operation"] = capo_lightsail.types.operation.serialize_aws_json_1_1(
            value["operation"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteDomainEntryResult:
    out: DeleteDomainEntryResult = {}  # type: ignore[typeddict-item]
    if "operation" in data:
        import capo_lightsail.types.operation

        out["operation"] = capo_lightsail.types.operation.deserialize_aws_json_1_1(
            data["operation"]
        )
    return out
