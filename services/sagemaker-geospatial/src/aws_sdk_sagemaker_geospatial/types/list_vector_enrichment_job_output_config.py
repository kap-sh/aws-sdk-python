"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ListVectorEnrichmentJobOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_sagemaker_geospatial.types.tags
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_status
    import aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_type


class ListVectorEnrichmentJobOutputConfig(TypedDict):
    arn: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_arn.VectorEnrichmentJobArn"
    """<p>The Amazon Resource Name (ARN) of the list of the Vector Enrichment jobs.</p>"""
    name: "str"
    """<p>The names of the Vector Enrichment jobs in the list.</p>"""
    type: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_type.VectorEnrichmentJobType"
    """<p>The type of the list of Vector Enrichment jobs.</p>"""
    creation_time: "datetime.datetime"
    """<p>The creation time.</p>"""
    duration_in_seconds: "int"
    """<p>The duration of the session, in seconds.</p>"""
    status: "aws_sdk_sagemaker_geospatial.types.vector_enrichment_job_status.VectorEnrichmentJobStatus"
    """<p>The status of the Vector Enrichment jobs list. </p>"""
    tags: NotRequired["aws_sdk_sagemaker_geospatial.types.tags.Tags"]
    """<p>Each tag consists of a key and a value.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListVectorEnrichmentJobOutputConfig) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["Name"] = value["name"]
    out["Type"] = value["type"]
    import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

    out["CreationTime"] = (
        aws_sdk_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["creation_time"]
        )
    )
    out["DurationInSeconds"] = value["duration_in_seconds"]
    out["Status"] = value["status"]
    if "tags" in value:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["Tags"] = aws_sdk_sagemaker_geospatial.types.tags.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> ListVectorEnrichmentJobOutputConfig:
    out: ListVectorEnrichmentJobOutputConfig = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("ListVectorEnrichmentJobOutputConfig.arn required")
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("ListVectorEnrichmentJobOutputConfig.name required")
    if "Type" in data:
        out["type"] = data["Type"]
    else:
        raise DeserializationError("ListVectorEnrichmentJobOutputConfig.type required")
    if "CreationTime" in data:
        import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["CreationTime"]
            )
        )
    else:
        raise DeserializationError(
            "ListVectorEnrichmentJobOutputConfig.creation_time required"
        )
    if "DurationInSeconds" in data:
        out["duration_in_seconds"] = data["DurationInSeconds"]
    else:
        raise DeserializationError(
            "ListVectorEnrichmentJobOutputConfig.duration_in_seconds required"
        )
    if "Status" in data:
        out["status"] = data["Status"]
    else:
        raise DeserializationError(
            "ListVectorEnrichmentJobOutputConfig.status required"
        )
    if "Tags" in data:
        import aws_sdk_sagemaker_geospatial.types.tags

        out["tags"] = aws_sdk_sagemaker_geospatial.types.tags.deserialize_json(
            data["Tags"]
        )
    return out
