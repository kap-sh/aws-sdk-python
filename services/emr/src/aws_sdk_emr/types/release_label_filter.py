"""Generated from Smithy shape ``com.amazonaws.emr#ReleaseLabelFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.string


class ReleaseLabelFilter(TypedDict):
    prefix: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>Optional release label version prefix filter. For example, <code>emr-5</code>.</p>"""
    application: NotRequired["aws_sdk_emr.types.string.String"]
    """<p>Optional release label application filter. For example, <code>spark@2.1.0</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReleaseLabelFilter) -> dict:
    out: dict = {}
    if "prefix" in value:
        out["Prefix"] = value["prefix"]
    if "application" in value:
        out["Application"] = value["application"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ReleaseLabelFilter:
    out: ReleaseLabelFilter = {}  # type: ignore[typeddict-item]
    if "Prefix" in data:
        out["prefix"] = data["Prefix"]
    if "Application" in data:
        out["application"] = data["Application"]
    return out
