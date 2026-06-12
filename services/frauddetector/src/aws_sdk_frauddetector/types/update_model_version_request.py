"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateModelVersionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.external_events_detail
    import aws_sdk_frauddetector.types.ingested_events_detail
    import aws_sdk_frauddetector.types.model_identifier
    import aws_sdk_frauddetector.types.model_type_enum
    import aws_sdk_frauddetector.types.tag_list
    import aws_sdk_frauddetector.types.whole_number_version_string


class UpdateModelVersionRequest(TypedDict):
    model_id: "aws_sdk_frauddetector.types.model_identifier.modelIdentifier"
    """<p>The model ID.</p>"""
    model_type: "aws_sdk_frauddetector.types.model_type_enum.ModelTypeEnum"
    """<p>The model type.</p>"""
    major_version_number: "aws_sdk_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    """<p>The major version number.</p>"""
    external_events_detail: NotRequired[
        "aws_sdk_frauddetector.types.external_events_detail.ExternalEventsDetail"
    ]
    """<p>The details of the external events data used for training the model version. Required if <code>trainingDataSource</code> is <code>EXTERNAL_EVENTS</code>.</p>"""
    ingested_events_detail: NotRequired[
        "aws_sdk_frauddetector.types.ingested_events_detail.IngestedEventsDetail"
    ]
    """<p>The details of the ingested event used for training the model version. Required if your <code>trainingDataSource</code> is <code>INGESTED_EVENTS</code>.</p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateModelVersionRequest) -> dict:
    out: dict = {}
    out["modelId"] = value["model_id"]
    import aws_sdk_frauddetector.types.model_type_enum

    out["modelType"] = (
        aws_sdk_frauddetector.types.model_type_enum.serialize_aws_json_1_1(
            value["model_type"]
        )
    )
    out["majorVersionNumber"] = value["major_version_number"]
    if "external_events_detail" in value:
        import aws_sdk_frauddetector.types.external_events_detail

        out["externalEventsDetail"] = (
            aws_sdk_frauddetector.types.external_events_detail.serialize_aws_json_1_1(
                value["external_events_detail"]
            )
        )
    if "ingested_events_detail" in value:
        import aws_sdk_frauddetector.types.ingested_events_detail

        out["ingestedEventsDetail"] = (
            aws_sdk_frauddetector.types.ingested_events_detail.serialize_aws_json_1_1(
                value["ingested_events_detail"]
            )
        )
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateModelVersionRequest:
    out: UpdateModelVersionRequest = {}  # type: ignore[typeddict-item]
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError("UpdateModelVersionRequest.model_id required")
    if "modelType" in data:
        import aws_sdk_frauddetector.types.model_type_enum

        out["model_type"] = (
            aws_sdk_frauddetector.types.model_type_enum.deserialize_aws_json_1_1(
                data["modelType"]
            )
        )
    else:
        raise DeserializationError("UpdateModelVersionRequest.model_type required")
    if "majorVersionNumber" in data:
        out["major_version_number"] = data["majorVersionNumber"]
    else:
        raise DeserializationError(
            "UpdateModelVersionRequest.major_version_number required"
        )
    if "externalEventsDetail" in data:
        import aws_sdk_frauddetector.types.external_events_detail

        out["external_events_detail"] = (
            aws_sdk_frauddetector.types.external_events_detail.deserialize_aws_json_1_1(
                data["externalEventsDetail"]
            )
        )
    if "ingestedEventsDetail" in data:
        import aws_sdk_frauddetector.types.ingested_events_detail

        out["ingested_events_detail"] = (
            aws_sdk_frauddetector.types.ingested_events_detail.deserialize_aws_json_1_1(
                data["ingestedEventsDetail"]
            )
        )
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
