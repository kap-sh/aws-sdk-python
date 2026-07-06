"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.finding_source_detail
    import aws_sdk_accessanalyzer.types.finding_source_type


class FindingSource(TypedDict, closed=True):
    type: "aws_sdk_accessanalyzer.types.finding_source_type.FindingSourceType"
    """<p>Indicates the type of access that generated the finding.</p>"""
    detail: NotRequired[
        "aws_sdk_accessanalyzer.types.finding_source_detail.FindingSourceDetail"
    ]
    """<p>Includes details about how the access that generated the finding is granted. This is populated for Amazon S3 bucket findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingSource) -> dict:
    out: dict = {}
    out["type"] = value["type"]
    if "detail" in value:
        import aws_sdk_accessanalyzer.types.finding_source_detail

        out["detail"] = (
            aws_sdk_accessanalyzer.types.finding_source_detail.serialize_json(
                value["detail"]
            )
        )
    return out


def deserialize_json(data: dict) -> FindingSource:
    out: FindingSource = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("FindingSource.type required")
    if "detail" in data:
        import aws_sdk_accessanalyzer.types.finding_source_detail

        out["detail"] = (
            aws_sdk_accessanalyzer.types.finding_source_detail.deserialize_json(
                data["detail"]
            )
        )
    return out
