"""Generated from Smithy shape ``com.amazonaws.emr#DescribeStudioOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.studio


class DescribeStudioOutput(TypedDict, closed=True):
    studio: NotRequired["capo_emr.types.studio.Studio"]
    """<p>The Amazon EMR Studio details.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStudioOutput) -> dict:
    out: dict = {}
    if "studio" in value:
        import capo_emr.types.studio

        out["Studio"] = capo_emr.types.studio.serialize_aws_json_1_1(value["studio"])
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStudioOutput:
    out: DescribeStudioOutput = {}  # type: ignore[typeddict-item]
    if "Studio" in data:
        import capo_emr.types.studio

        out["studio"] = capo_emr.types.studio.deserialize_aws_json_1_1(data["Studio"])
    return out
