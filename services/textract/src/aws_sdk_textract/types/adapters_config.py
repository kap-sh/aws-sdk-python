"""Generated from Smithy shape ``com.amazonaws.textract#AdaptersConfig``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_textract.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_textract.types.adapters


class AdaptersConfig(TypedDict):
    adapters: "aws_sdk_textract.types.adapters.Adapters"
    """<p>A list of adapters to be used when analyzing the specified document.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AdaptersConfig) -> dict:
    out: dict = {}
    import aws_sdk_textract.types.adapters

    out["Adapters"] = aws_sdk_textract.types.adapters.serialize_aws_json_1_1(
        value["adapters"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AdaptersConfig:
    out: AdaptersConfig = {}  # type: ignore[typeddict-item]
    if "Adapters" in data:
        import aws_sdk_textract.types.adapters

        out["adapters"] = aws_sdk_textract.types.adapters.deserialize_aws_json_1_1(
            data["Adapters"]
        )
    else:
        raise DeserializationError("AdaptersConfig.adapters required")
    return out
