"""Generated from Smithy shape ``com.amazonaws.emr#DescribeStudioOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.studio


class DescribeStudioOutput(TypedDict):
    studio: NotRequired["aws_sdk_emr.types.studio.Studio"]
    """<p>The Amazon EMR Studio details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStudioOutput) -> dict:
    out: dict = {}
    if "studio" in value:
        import aws_sdk_emr.types.studio

        out["Studio"] = aws_sdk_emr.types.studio.serialize_aws_json_1_1(value["studio"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStudioOutput:
    out: DescribeStudioOutput = {}  # type: ignore[typeddict-item]
    if "Studio" in data:
        import aws_sdk_emr.types.studio

        out["studio"] = aws_sdk_emr.types.studio.deserialize_aws_json_1_1(
            data["Studio"]
        )
    return out
