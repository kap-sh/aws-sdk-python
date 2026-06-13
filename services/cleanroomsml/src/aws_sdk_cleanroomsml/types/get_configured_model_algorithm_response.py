"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredModelAlgorithmResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_cleanroomsml.types.configured_model_algorithm_arn
    import aws_sdk_cleanroomsml.types.container_config
    import aws_sdk_cleanroomsml.types.iam_role_arn
    import aws_sdk_cleanroomsml.types.inference_container_config
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map


class GetConfiguredModelAlgorithmResponse(TypedDict):
    create_time: "datetime.datetime"
    """<p>The time at which the configured model algorithm was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured model algorithm was updated.</p>"""
    configured_model_algorithm_arn: "aws_sdk_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm.</p>"""
    training_container_config: NotRequired[
        "aws_sdk_cleanroomsml.types.container_config.ContainerConfig"
    ]
    """<p>The configuration information of the training container for the configured model algorithm.</p>"""
    inference_container_config: NotRequired[
        "aws_sdk_cleanroomsml.types.inference_container_config.InferenceContainerConfig"
    ]
    """<p>Configuration information for the inference container.</p>"""
    role_arn: "aws_sdk_cleanroomsml.types.iam_role_arn.IamRoleArn"
    """<p>The Amazon Resource Name (ARN) of the service role that was used to create the configured model algorithm.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    kms_key_arn: NotRequired["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key. This key is used to encrypt and decrypt customer-owned data in the configured ML model and associated data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredModelAlgorithmResponse) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["createTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import aws_sdk_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = aws_sdk_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["name"] = value["name"]
    if "training_container_config" in value:
        import aws_sdk_cleanroomsml.types.container_config

        out["trainingContainerConfig"] = (
            aws_sdk_cleanroomsml.types.container_config.serialize_json(
                value["training_container_config"]
            )
        )
    if "inference_container_config" in value:
        import aws_sdk_cleanroomsml.types.inference_container_config

        out["inferenceContainerConfig"] = (
            aws_sdk_cleanroomsml.types.inference_container_config.serialize_json(
                value["inference_container_config"]
            )
        )
    out["roleArn"] = value["role_arn"]
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    return out


def deserialize_json(data: dict) -> GetConfiguredModelAlgorithmResponse:
    out: GetConfiguredModelAlgorithmResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmResponse.create_time required"
        )
    if "updateTime" in data:
        import aws_sdk_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            aws_sdk_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmResponse.update_time required"
        )
    if "configuredModelAlgorithmArn" in data:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmResponse.configured_model_algorithm_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetConfiguredModelAlgorithmResponse.name required")
    if "trainingContainerConfig" in data:
        import aws_sdk_cleanroomsml.types.container_config

        out["training_container_config"] = (
            aws_sdk_cleanroomsml.types.container_config.deserialize_json(
                data["trainingContainerConfig"]
            )
        )
    if "inferenceContainerConfig" in data:
        import aws_sdk_cleanroomsml.types.inference_container_config

        out["inference_container_config"] = (
            aws_sdk_cleanroomsml.types.inference_container_config.deserialize_json(
                data["inferenceContainerConfig"]
            )
        )
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmResponse.role_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    return out
