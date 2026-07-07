"""Generated from Smithy shape ``com.amazonaws.proton#CreateServiceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_proton.types.service


class CreateServiceOutput(TypedDict, closed=True):
    service: "aws_sdk_proton.types.service.Service"
    """<p>The service detail data that's returned by Proton.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateServiceOutput) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.service

    out["service"] = aws_sdk_proton.types.service.serialize_aws_json_1_0(
        value["service"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateServiceOutput:
    out: CreateServiceOutput = {}  # type: ignore[typeddict-item]
    if "service" in data:
        import aws_sdk_proton.types.service

        out["service"] = aws_sdk_proton.types.service.deserialize_aws_json_1_0(
            data["service"]
        )
    else:
        raise DeserializationError("CreateServiceOutput.service required")
    return out
