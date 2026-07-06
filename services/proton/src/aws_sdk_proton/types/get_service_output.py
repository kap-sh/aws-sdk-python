"""Generated from Smithy shape ``com.amazonaws.proton#GetServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.service


class GetServiceOutput(TypedDict, closed=True):
    service: NotRequired["aws_sdk_proton.types.service.Service"]
    """<p>The detailed data of the requested service.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetServiceOutput) -> dict:
    out: dict = {}
    if "service" in value:
        import aws_sdk_proton.types.service

        out["service"] = aws_sdk_proton.types.service.serialize_aws_json_1_0(
            value["service"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetServiceOutput:
    out: GetServiceOutput = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_proton.types.service

        out["service"] = aws_sdk_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    return out
