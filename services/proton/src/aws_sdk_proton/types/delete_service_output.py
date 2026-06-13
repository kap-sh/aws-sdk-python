"""Generated from Smithy shape ``com.amazonaws.proton#DeleteServiceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_proton.types.service


class DeleteServiceOutput(TypedDict):
    service: NotRequired["aws_sdk_proton.types.service.Service"]
    """<p>The detailed data of the service being deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteServiceOutput) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_proton.types.service

        out["service"] = aws_sdk_proton.types.service.serialize_aws_json_1_0(
            value["service"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteServiceOutput:
    out: DeleteServiceOutput = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_proton.types.service

        out["service"] = aws_sdk_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    return out
