"""Generated from Smithy shape ``com.amazonaws.comprehendmedical#DetectPHIResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_comprehendmedical.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_comprehendmedical.types.entity_list
    import aws_sdk_comprehendmedical.types.string


class DetectPHIResponse(TypedDict, closed=True):
    entities: "aws_sdk_comprehendmedical.types.entity_list.EntityList"
    """<p>The collection of PHI entities extracted from the input text and their associated information. For each entity, the response provides the entity text, the entity category, where the entity text begins and ends, and the level of confidence that Amazon Comprehend Medical has in its detection.</p>"""
    pagination_token: NotRequired["aws_sdk_comprehendmedical.types.string.String"]
    """<p>If the result of the previous request to <code>DetectPHI</code> was truncated, include the <code>PaginationToken</code> to fetch the next page of PHI entities. </p>"""
    model_version: "aws_sdk_comprehendmedical.types.string.String"
    """<p>The version of the model used to analyze the documents. The version number looks like X.X.X. You can use this information to track the model used for a particular batch of documents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DetectPHIResponse) -> dict:
    out: dict = {}
    import aws_sdk_comprehendmedical.types.entity_list

    out["Entities"] = (
        aws_sdk_comprehendmedical.types.entity_list.serialize_aws_json_1_1(
            value["entities"]
        )
    )
    if "pagination_token" in value:
        out["PaginationToken"] = value["pagination_token"]
    out["ModelVersion"] = value["model_version"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DetectPHIResponse:
    out: DetectPHIResponse = {}  # type: ignore[typeddict-item]
    if "Entities" in data:
        import aws_sdk_comprehendmedical.types.entity_list

        out["entities"] = (
            aws_sdk_comprehendmedical.types.entity_list.deserialize_aws_json_1_1(
                data["Entities"]
            )
        )
    else:
        raise DeserializationError("DetectPHIResponse.entities required")
    if "PaginationToken" in data:
        out["pagination_token"] = data["PaginationToken"]
    if "ModelVersion" in data:
        out["model_version"] = data["ModelVersion"]
    else:
        raise DeserializationError("DetectPHIResponse.model_version required")
    return out
