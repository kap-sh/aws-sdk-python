"""Generated from Smithy shape ``com.amazonaws.personalize#CreateDatasetGroupResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_personalize.types.arn
    import capo_personalize.types.domain


class CreateDatasetGroupResponse(TypedDict, closed=True):
    dataset_group_arn: NotRequired["capo_personalize.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the new dataset group.</p>"""
    domain: NotRequired["capo_personalize.types.domain.Domain"]
    """<p>The domain for the new Domain dataset group.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDatasetGroupResponse) -> dict:
    out: dict = {}
    if "dataset_group_arn" in value:
        out["datasetGroupArn"] = value["dataset_group_arn"]
    if "domain" in value:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.serialize_aws_json_1_1(
            value["domain"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDatasetGroupResponse:
    out: CreateDatasetGroupResponse = {}  # type: ignore[typeddict-item]
    if "datasetGroupArn" in data:
        out["dataset_group_arn"] = data["datasetGroupArn"]
    if "domain" in data:
        import capo_personalize.types.domain

        out["domain"] = capo_personalize.types.domain.deserialize_aws_json_1_1(
            data["domain"]
        )
    return out
