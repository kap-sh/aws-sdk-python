"""Generated from Smithy shape ``com.amazonaws.bedrock#CreateProvisionedModelThroughputRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.commitment_duration
    import aws_sdk_bedrock.types.idempotency_token
    import aws_sdk_bedrock.types.model_identifier
    import aws_sdk_bedrock.types.positive_integer
    import aws_sdk_bedrock.types.provisioned_model_name
    import aws_sdk_bedrock.types.tag_list


class CreateProvisionedModelThroughputRequest(TypedDict):
    client_request_token: NotRequired[
        "aws_sdk_bedrock.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a> in the Amazon S3 User Guide.</p>"""
    model_units: "aws_sdk_bedrock.types.positive_integer.PositiveInteger"
    """<p>Number of model units to allocate. A model unit delivers a specific throughput level for the specified model. The throughput level of a model unit specifies the total number of input and output tokens that it can process and generate within a span of one minute. By default, your account has no model units for purchasing Provisioned Throughputs with commitment. You must first visit the <a href=\"https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase\">Amazon Web Services support center</a> to request MUs.</p> <p>For model unit quotas, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html#prov-thru-quotas\">Provisioned Throughput quotas</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p> <p>For more information about what an MU specifies, contact your Amazon Web Services account manager.</p>"""
    provisioned_model_name: (
        "aws_sdk_bedrock.types.provisioned_model_name.ProvisionedModelName"
    )
    """<p>The name for this Provisioned Throughput.</p>"""
    model_id: "aws_sdk_bedrock.types.model_identifier.ModelIdentifier"
    """<p>The Amazon Resource Name (ARN) or name of the model to associate with this Provisioned Throughput. For a list of models for which you can purchase Provisioned Throughput, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#prov-throughput-models\">Amazon Bedrock model IDs for purchasing Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a>.</p>"""
    commitment_duration: NotRequired[
        "aws_sdk_bedrock.types.commitment_duration.CommitmentDuration"
    ]
    """<p>The commitment duration requested for the Provisioned Throughput. Billing occurs hourly and is discounted for longer commitment terms. To request a no-commit Provisioned Throughput, omit this field.</p> <p>Custom models support all levels of commitment. To see which base models support no commitment, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/pt-supported.html\">Supported regions and models for Provisioned Throughput</a> in the <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-service.html\">Amazon Bedrock User Guide</a> </p>"""
    tags: NotRequired["aws_sdk_bedrock.types.tag_list.TagList"]
    """<p>Tags to associate with this Provisioned Throughput.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisionedModelThroughputRequest) -> dict:
    out: dict = {}
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    out["modelUnits"] = value["model_units"]
    out["provisionedModelName"] = value["provisioned_model_name"]
    out["modelId"] = value["model_id"]
    if "commitment_duration" in value:
        import aws_sdk_bedrock.types.commitment_duration

        out["commitmentDuration"] = (
            aws_sdk_bedrock.types.commitment_duration.serialize_json(
                value["commitment_duration"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateProvisionedModelThroughputRequest:
    out: CreateProvisionedModelThroughputRequest = {}  # type: ignore[typeddict-item]
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    if "modelUnits" in data:
        out["model_units"] = data["modelUnits"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputRequest.model_units required"
        )
    if "provisionedModelName" in data:
        out["provisioned_model_name"] = data["provisionedModelName"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputRequest.provisioned_model_name required"
        )
    if "modelId" in data:
        out["model_id"] = data["modelId"]
    else:
        raise DeserializationError(
            "CreateProvisionedModelThroughputRequest.model_id required"
        )
    if "commitmentDuration" in data:
        import aws_sdk_bedrock.types.commitment_duration

        out["commitment_duration"] = (
            aws_sdk_bedrock.types.commitment_duration.deserialize_json(
                data["commitmentDuration"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock.types.tag_list

        out["tags"] = aws_sdk_bedrock.types.tag_list.deserialize_json(data["tags"])
    return out
