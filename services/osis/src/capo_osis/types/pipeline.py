"""Generated from Smithy shape ``com.amazonaws.osis#Pipeline``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_osis.types.buffer_options
    import capo_osis.types.encryption_at_rest_options
    import capo_osis.types.ingest_endpoint_urls_list
    import capo_osis.types.integer
    import capo_osis.types.log_publishing_options
    import capo_osis.types.pipeline_destination_list
    import capo_osis.types.pipeline_role_arn
    import capo_osis.types.pipeline_status
    import capo_osis.types.pipeline_status_reason
    import capo_osis.types.service_vpc_endpoints_list
    import capo_osis.types.string
    import capo_osis.types.tag_list
    import capo_osis.types.timestamp
    import capo_osis.types.vpc_endpoints_list


class Pipeline(TypedDict, closed=True):
    pipeline_name: NotRequired["capo_osis.types.string.String"]
    """<p>The name of the pipeline.</p>"""
    pipeline_arn: NotRequired["capo_osis.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the pipeline.</p>"""
    min_units: "capo_osis.types.integer.Integer"
    """<p>The minimum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    max_units: "capo_osis.types.integer.Integer"
    """<p>The maximum pipeline capacity, in Ingestion Compute Units (ICUs).</p>"""
    status: NotRequired["capo_osis.types.pipeline_status.PipelineStatus"]
    """<p>The current status of the pipeline.</p>"""
    status_reason: NotRequired[
        "capo_osis.types.pipeline_status_reason.PipelineStatusReason"
    ]
    """<p>The reason for the current status of the pipeline.</p>"""
    pipeline_configuration_body: NotRequired["capo_osis.types.string.String"]
    """<p>The Data Prepper pipeline configuration in YAML format.</p>"""
    created_at: NotRequired["capo_osis.types.timestamp.Timestamp"]
    """<p>The date and time when the pipeline was created.</p>"""
    last_updated_at: NotRequired["capo_osis.types.timestamp.Timestamp"]
    """<p>The date and time when the pipeline was last updated.</p>"""
    ingest_endpoint_urls: NotRequired[
        "capo_osis.types.ingest_endpoint_urls_list.IngestEndpointUrlsList"
    ]
    """<p>The ingestion endpoints for the pipeline, which you can send data to.</p>"""
    log_publishing_options: NotRequired[
        "capo_osis.types.log_publishing_options.LogPublishingOptions"
    ]
    """<p>Key-value pairs that represent log publishing settings.</p>"""
    vpc_endpoints: NotRequired["capo_osis.types.vpc_endpoints_list.VpcEndpointsList"]
    """<p>The VPC interface endpoints that have access to the pipeline.</p>"""
    buffer_options: NotRequired["capo_osis.types.buffer_options.BufferOptions"]
    encryption_at_rest_options: NotRequired[
        "capo_osis.types.encryption_at_rest_options.EncryptionAtRestOptions"
    ]
    vpc_endpoint_service: NotRequired["capo_osis.types.string.String"]
    """<p>The VPC endpoint service name for the pipeline.</p>"""
    service_vpc_endpoints: NotRequired[
        "capo_osis.types.service_vpc_endpoints_list.ServiceVpcEndpointsList"
    ]
    """<p>A list of VPC endpoints that OpenSearch Ingestion has created to other Amazon Web Services services.</p>"""
    destinations: NotRequired[
        "capo_osis.types.pipeline_destination_list.PipelineDestinationList"
    ]
    """<p>Destinations to which the pipeline writes data.</p>"""
    tags: NotRequired["capo_osis.types.tag_list.TagList"]
    """<p>A list of tags associated with the given pipeline.</p>"""
    pipeline_role_arn: NotRequired["capo_osis.types.pipeline_role_arn.PipelineRoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that the pipeline uses to access AWS resources.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Pipeline) -> dict:
    out: dict = {}
    if "pipeline_name" in value:
        out["PipelineName"] = value["pipeline_name"]
    if "pipeline_arn" in value:
        out["PipelineArn"] = value["pipeline_arn"]
    out["MinUnits"] = value.get("min_units", 0)
    out["MaxUnits"] = value.get("max_units", 0)
    if "status" in value:
        import capo_osis.types.pipeline_status

        out["Status"] = capo_osis.types.pipeline_status.serialize_json(value["status"])
    if "status_reason" in value:
        import capo_osis.types.pipeline_status_reason

        out["StatusReason"] = capo_osis.types.pipeline_status_reason.serialize_json(
            value["status_reason"]
        )
    if "pipeline_configuration_body" in value:
        out["PipelineConfigurationBody"] = value["pipeline_configuration_body"]
    if "created_at" in value:
        import capo_osis.types.timestamp

        out["CreatedAt"] = capo_osis.types.timestamp.serialize_json(value["created_at"])
    if "last_updated_at" in value:
        import capo_osis.types.timestamp

        out["LastUpdatedAt"] = capo_osis.types.timestamp.serialize_json(
            value["last_updated_at"]
        )
    if "ingest_endpoint_urls" in value:
        import capo_osis.types.ingest_endpoint_urls_list

        out["IngestEndpointUrls"] = (
            capo_osis.types.ingest_endpoint_urls_list.serialize_json(
                value["ingest_endpoint_urls"]
            )
        )
    if "log_publishing_options" in value:
        import capo_osis.types.log_publishing_options

        out["LogPublishingOptions"] = (
            capo_osis.types.log_publishing_options.serialize_json(
                value["log_publishing_options"]
            )
        )
    if "vpc_endpoints" in value:
        import capo_osis.types.vpc_endpoints_list

        out["VpcEndpoints"] = capo_osis.types.vpc_endpoints_list.serialize_json(
            value["vpc_endpoints"]
        )
    if "buffer_options" in value:
        import capo_osis.types.buffer_options

        out["BufferOptions"] = capo_osis.types.buffer_options.serialize_json(
            value["buffer_options"]
        )
    if "encryption_at_rest_options" in value:
        import capo_osis.types.encryption_at_rest_options

        out["EncryptionAtRestOptions"] = (
            capo_osis.types.encryption_at_rest_options.serialize_json(
                value["encryption_at_rest_options"]
            )
        )
    if "vpc_endpoint_service" in value:
        out["VpcEndpointService"] = value["vpc_endpoint_service"]
    if "service_vpc_endpoints" in value:
        import capo_osis.types.service_vpc_endpoints_list

        out["ServiceVpcEndpoints"] = (
            capo_osis.types.service_vpc_endpoints_list.serialize_json(
                value["service_vpc_endpoints"]
            )
        )
    if "destinations" in value:
        import capo_osis.types.pipeline_destination_list

        out["Destinations"] = capo_osis.types.pipeline_destination_list.serialize_json(
            value["destinations"]
        )
    if "tags" in value:
        import capo_osis.types.tag_list

        out["Tags"] = capo_osis.types.tag_list.serialize_json(value["tags"])
    if "pipeline_role_arn" in value:
        out["PipelineRoleArn"] = value["pipeline_role_arn"]
    return out


def deserialize_json(data: dict) -> Pipeline:
    out: Pipeline = {}  # type: ignore[typeddict-item]
    if "PipelineName" in data:
        out["pipeline_name"] = data["PipelineName"]
    if "PipelineArn" in data:
        out["pipeline_arn"] = data["PipelineArn"]
    if "MinUnits" in data:
        out["min_units"] = data["MinUnits"]
    else:
        out["min_units"] = 0
    if "MaxUnits" in data:
        out["max_units"] = data["MaxUnits"]
    else:
        out["max_units"] = 0
    if "Status" in data:
        import capo_osis.types.pipeline_status

        out["status"] = capo_osis.types.pipeline_status.deserialize_json(data["Status"])
    if "StatusReason" in data:
        import capo_osis.types.pipeline_status_reason

        out["status_reason"] = capo_osis.types.pipeline_status_reason.deserialize_json(
            data["StatusReason"]
        )
    if "PipelineConfigurationBody" in data:
        out["pipeline_configuration_body"] = data["PipelineConfigurationBody"]
    if "CreatedAt" in data:
        import capo_osis.types.timestamp

        out["created_at"] = capo_osis.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "LastUpdatedAt" in data:
        import capo_osis.types.timestamp

        out["last_updated_at"] = capo_osis.types.timestamp.deserialize_json(
            data["LastUpdatedAt"]
        )
    if "IngestEndpointUrls" in data:
        import capo_osis.types.ingest_endpoint_urls_list

        out["ingest_endpoint_urls"] = (
            capo_osis.types.ingest_endpoint_urls_list.deserialize_json(
                data["IngestEndpointUrls"]
            )
        )
    if "LogPublishingOptions" in data:
        import capo_osis.types.log_publishing_options

        out["log_publishing_options"] = (
            capo_osis.types.log_publishing_options.deserialize_json(
                data["LogPublishingOptions"]
            )
        )
    if "VpcEndpoints" in data:
        import capo_osis.types.vpc_endpoints_list

        out["vpc_endpoints"] = capo_osis.types.vpc_endpoints_list.deserialize_json(
            data["VpcEndpoints"]
        )
    if "BufferOptions" in data:
        import capo_osis.types.buffer_options

        out["buffer_options"] = capo_osis.types.buffer_options.deserialize_json(
            data["BufferOptions"]
        )
    if "EncryptionAtRestOptions" in data:
        import capo_osis.types.encryption_at_rest_options

        out["encryption_at_rest_options"] = (
            capo_osis.types.encryption_at_rest_options.deserialize_json(
                data["EncryptionAtRestOptions"]
            )
        )
    if "VpcEndpointService" in data:
        out["vpc_endpoint_service"] = data["VpcEndpointService"]
    if "ServiceVpcEndpoints" in data:
        import capo_osis.types.service_vpc_endpoints_list

        out["service_vpc_endpoints"] = (
            capo_osis.types.service_vpc_endpoints_list.deserialize_json(
                data["ServiceVpcEndpoints"]
            )
        )
    if "Destinations" in data:
        import capo_osis.types.pipeline_destination_list

        out["destinations"] = (
            capo_osis.types.pipeline_destination_list.deserialize_json(
                data["Destinations"]
            )
        )
    if "Tags" in data:
        import capo_osis.types.tag_list

        out["tags"] = capo_osis.types.tag_list.deserialize_json(data["Tags"])
    if "PipelineRoleArn" in data:
        out["pipeline_role_arn"] = data["PipelineRoleArn"]
    return out
