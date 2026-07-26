"""Generated from Smithy shape ``com.amazonaws.sagemaker#KendraSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.feature_status


class KendraSettings(TypedDict, closed=True):
    status: NotRequired["capo_sagemaker.types.feature_status.FeatureStatus"]
    """<p>Describes whether the document querying feature is enabled or disabled in the Canvas application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KendraSettings) -> dict:
    out: dict = {}
    if "status" in value:
        import capo_sagemaker.types.feature_status

        out["Status"] = capo_sagemaker.types.feature_status.serialize_aws_json_1_1(
            value["status"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KendraSettings:
    out: KendraSettings = {}  # type: ignore[typeddict-item]
    if "Status" in data:
        import capo_sagemaker.types.feature_status

        out["status"] = capo_sagemaker.types.feature_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    return out
