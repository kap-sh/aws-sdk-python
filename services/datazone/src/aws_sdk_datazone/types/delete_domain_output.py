"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteDomainOutput``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_datazone.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_status


class DeleteDomainOutput(TypedDict):
    status: "aws_sdk_datazone.types.domain_status.DomainStatus"
    """<p>The status of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDomainOutput) -> dict:
    out: dict = {}
    import aws_sdk_datazone.types.domain_status

    out["status"] = aws_sdk_datazone.types.domain_status.serialize_json(value["status"])
    return out


def deserialize_json(data: dict) -> DeleteDomainOutput:
    out: DeleteDomainOutput = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_datazone.types.domain_status

        out["status"] = aws_sdk_datazone.types.domain_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("DeleteDomainOutput.status required")
    return out
