"""Generated from Smithy shape ``com.amazonaws.emr#DescribeStudioInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_max_len256


class DescribeStudioInput(TypedDict, closed=True):
    studio_id: NotRequired["aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"]
    """<p>The Amazon EMR Studio ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeStudioInput) -> dict:
    out: dict = {}
    if "studio_id" in value:
        out["StudioId"] = value["studio_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeStudioInput:
    out: DescribeStudioInput = {}  # type: ignore[typeddict-item]
    if "StudioId" in data:
        out["studio_id"] = data["StudioId"]
    return out
