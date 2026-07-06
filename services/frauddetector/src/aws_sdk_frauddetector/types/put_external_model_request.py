"""Generated from Smithy shape ``com.amazonaws.frauddetector#PutExternalModelRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.model_endpoint_status
    import aws_sdk_frauddetector.types.model_input_configuration
    import aws_sdk_frauddetector.types.model_output_configuration
    import aws_sdk_frauddetector.types.model_source
    import aws_sdk_frauddetector.types.sage_maker_endpoint_identifier
    import aws_sdk_frauddetector.types.string
    import aws_sdk_frauddetector.types.tag_list


class PutExternalModelRequest(TypedDict, closed=True):
    model_endpoint: "aws_sdk_frauddetector.types.sage_maker_endpoint_identifier.sageMakerEndpointIdentifier"
    """<p>The model endpoints name.</p>"""
    model_source: "aws_sdk_frauddetector.types.model_source.ModelSource"
    """<p>The source of the model.</p>"""
    invoke_model_endpoint_role_arn: "aws_sdk_frauddetector.types.string.string"
    """<p>The IAM role used to invoke the model endpoint.</p>"""
    input_configuration: (
        "aws_sdk_frauddetector.types.model_input_configuration.ModelInputConfiguration"
    )
    """<p>The model endpoint input configuration.</p>"""
    output_configuration: "aws_sdk_frauddetector.types.model_output_configuration.ModelOutputConfiguration"
    """<p>The model endpoint output configuration.</p>"""
    model_endpoint_status: (
        "aws_sdk_frauddetector.types.model_endpoint_status.ModelEndpointStatus"
    )
    """<p>The model endpoint’s status in Amazon Fraud Detector.</p>"""
    tags: NotRequired["aws_sdk_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutExternalModelRequest) -> dict:
    out: dict = {}
    out["modelEndpoint"] = value["model_endpoint"]
    import aws_sdk_frauddetector.types.model_source

    out["modelSource"] = (
        aws_sdk_frauddetector.types.model_source.serialize_aws_json_1_1(
            value["model_source"]
        )
    )
    out["invokeModelEndpointRoleArn"] = value["invoke_model_endpoint_role_arn"]
    import aws_sdk_frauddetector.types.model_input_configuration

    out["inputConfiguration"] = (
        aws_sdk_frauddetector.types.model_input_configuration.serialize_aws_json_1_1(
            value["input_configuration"]
        )
    )
    import aws_sdk_frauddetector.types.model_output_configuration

    out["outputConfiguration"] = (
        aws_sdk_frauddetector.types.model_output_configuration.serialize_aws_json_1_1(
            value["output_configuration"]
        )
    )
    import aws_sdk_frauddetector.types.model_endpoint_status

    out["modelEndpointStatus"] = (
        aws_sdk_frauddetector.types.model_endpoint_status.serialize_aws_json_1_1(
            value["model_endpoint_status"]
        )
    )
    if "tags" in value:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutExternalModelRequest:
    out: PutExternalModelRequest = {}  # type: ignore[typeddict-item]
    if "modelEndpoint" in data:
        out["model_endpoint"] = data["modelEndpoint"]
    else:
        raise DeserializationError("PutExternalModelRequest.model_endpoint required")
    if "modelSource" in data:
        import aws_sdk_frauddetector.types.model_source

        out["model_source"] = (
            aws_sdk_frauddetector.types.model_source.deserialize_aws_json_1_1(
                data["modelSource"]
            )
        )
    else:
        raise DeserializationError("PutExternalModelRequest.model_source required")
    if "invokeModelEndpointRoleArn" in data:
        out["invoke_model_endpoint_role_arn"] = data["invokeModelEndpointRoleArn"]
    else:
        raise DeserializationError(
            "PutExternalModelRequest.invoke_model_endpoint_role_arn required"
        )
    if "inputConfiguration" in data:
        import aws_sdk_frauddetector.types.model_input_configuration

        out["input_configuration"] = (
            aws_sdk_frauddetector.types.model_input_configuration.deserialize_aws_json_1_1(
                data["inputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalModelRequest.input_configuration required"
        )
    if "outputConfiguration" in data:
        import aws_sdk_frauddetector.types.model_output_configuration

        out["output_configuration"] = (
            aws_sdk_frauddetector.types.model_output_configuration.deserialize_aws_json_1_1(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalModelRequest.output_configuration required"
        )
    if "modelEndpointStatus" in data:
        import aws_sdk_frauddetector.types.model_endpoint_status

        out["model_endpoint_status"] = (
            aws_sdk_frauddetector.types.model_endpoint_status.deserialize_aws_json_1_1(
                data["modelEndpointStatus"]
            )
        )
    else:
        raise DeserializationError(
            "PutExternalModelRequest.model_endpoint_status required"
        )
    if "tags" in data:
        import aws_sdk_frauddetector.types.tag_list

        out["tags"] = aws_sdk_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out
