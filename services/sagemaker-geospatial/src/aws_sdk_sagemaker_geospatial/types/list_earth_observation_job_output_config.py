"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListEarthObservationJobOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_sagemaker_geospatial.types.earth_observation_job_status
    import aws_sdk_sagemaker_geospatial.types.tags


class ListEarthObservationJobOutputConfig(TypedDict):
    arn: "str"
    """<p>The Amazon Resource Name (ARN) of the list of the Earth Observation jobs.</p>"""
    name: "str"
    """<p>The names of the Earth Observation jobs in the list.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of the session, in seconds.</p>"""
    status: "aws_sdk_sagemaker_geospatial.types.earth_observation_job_status.EarthObservationJobStatus"
    """<p>The status of the list of the Earth Observation jobs.</p>"""
    operation_type: "str"
    """<p>The operation type for an Earth Observation job.</p>"""
    tags: NotRequired["aws_sdk_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEarthObservationJobOutputConfig) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

    out["CreationTime"] = (
        aws_sdk_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["DurationInSeconds"] = value["duration_in_seconds"]
    out["Status"] = value["status"]
    out["OperationType"] = value["operation_type"]
    if "tags" in value:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["Tags"] = aws_sdk_sagemaker_geospatial.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListEarthObservationJobOutputConfig:
    out: ListEarthObservationJobOutputConfig = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListEarthObservationJobOutputConfig.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ListEarthObservationJobOutputConfig.name required")
    if "CreationTime" in data:
        import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ListEarthObservationJobOutputConfig.creation_time required"
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "ListEarthObservationJobOutputConfig.duration_in_seconds required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError(
            "ListEarthObservationJobOutputConfig.status required"
        )
    if "OperationType" in data:
        out["operation_type"] = data["OperationType"]
    else:
        raise DeserializationError(
            "ListEarthObservationJobOutputConfig.operation_type required"
        )
    if "Tags" in data:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["tags"] = aws_sdk_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
