"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CreateMLInputChannelRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list
    import aws_sdk_cleanroomsml.types.input_channel
    import aws_sdk_cleanroomsml.types.kms_key_arn
    import aws_sdk_cleanroomsml.types.name_string
    import aws_sdk_cleanroomsml.types.payer_configuration
    import aws_sdk_cleanroomsml.types.resource_description
    import aws_sdk_cleanroomsml.types.tag_map
    import aws_sdk_cleanroomsml.types.uuid


class CreateMLInputChannelRequest(TypedDict):
    membership_identifier: "aws_sdk_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is creating the ML input channel.</p>"""
    configured_model_algorithm_associations: "aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.ConfiguredModelAlgorithmAssociationArnList"
    """<p>The associated configured model algorithms that are necessary to create this ML input channel.</p>"""
    input_channel: "aws_sdk_cleanroomsml.types.input_channel.InputChannel"
    """<p>The input data that is used to create this ML input channel.</p>"""
    name: "aws_sdk_cleanroomsml.types.name_string.NameString"
    """<p>The name of the ML input channel.</p>"""
    retention_in_days: "int"
    """<p>The number of days that the data in the ML input channel is retained.</p>"""
    description: NotRequired[
        "aws_sdk_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the ML input channel.</p>"""
    kms_key_arn: NotRequired["aws_sdk_cleanroomsml.types.kms_key_arn.KmsKeyArn"]
    """<p>The Amazon Resource Name (ARN) of the KMS key that is used to access the input channel.</p>"""
    tags: NotRequired["aws_sdk_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""
    payer_configuration: NotRequired[
        "aws_sdk_cleanroomsml.types.payer_configuration.PayerConfiguration"
    ]
    """<p>The payer configuration for the ML input channel. Determines which member account pays for compute and synthetic data costs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateMLInputChannelRequest) -> dict:
    out: dict = {}
    import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list

    out["configuredModelAlgorithmAssociations"] = (
        aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.serialize_json(
            value["configured_model_algorithm_associations"]
        )
    )
    import aws_sdk_cleanroomsml.types.input_channel

    out["inputChannel"] = aws_sdk_cleanroomsml.types.input_channel.serialize_json(
        value["input_channel"]
    )
    out["name"] = value["name"]
    out["retentionInDays"] = value["retention_in_days"]
    if "description" in value:
        out["description"] = value["description"]
    if "kms_key_arn" in value:
        out["kmsKeyArn"] = value["kms_key_arn"]
    if "tags" in value:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    if "payer_configuration" in value:
        import aws_sdk_cleanroomsml.types.payer_configuration

        out["payerConfiguration"] = (
            aws_sdk_cleanroomsml.types.payer_configuration.serialize_json(
                value["payer_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateMLInputChannelRequest:
    out: CreateMLInputChannelRequest = {}  # type: ignore[typeddict-item]
    if "configuredModelAlgorithmAssociations" in data:
        import aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list

        out["configured_model_algorithm_associations"] = (
            aws_sdk_cleanroomsml.types.configured_model_algorithm_association_arn_list.deserialize_json(
                data["configuredModelAlgorithmAssociations"]
            )
        )
    else:
        raise DeserializationError(
            "CreateMLInputChannelRequest.configured_model_algorithm_associations required"
        )
    if "inputChannel" in data:
        import aws_sdk_cleanroomsml.types.input_channel

        out["input_channel"] = (
            aws_sdk_cleanroomsml.types.input_channel.deserialize_json(
                data["inputChannel"]
            )
        )
    else:
        raise DeserializationError("CreateMLInputChannelRequest.input_channel required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateMLInputChannelRequest.name required")
    if "retentionInDays" in data:
        out["retention_in_days"] = data["retentionInDays"]
    else:
        raise DeserializationError(
            "CreateMLInputChannelRequest.retention_in_days required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "kmsKeyArn" in data:
        out["kms_key_arn"] = data["kmsKeyArn"]
    if "tags" in data:
        import aws_sdk_cleanroomsml.types.tag_map

        out["tags"] = aws_sdk_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    if "payerConfiguration" in data:
        import aws_sdk_cleanroomsml.types.payer_configuration

        out["payer_configuration"] = (
            aws_sdk_cleanroomsml.types.payer_configuration.deserialize_json(
                data["payerConfiguration"]
            )
        )
    return out
