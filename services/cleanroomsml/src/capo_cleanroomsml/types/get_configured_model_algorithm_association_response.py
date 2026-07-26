"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#GetConfiguredModelAlgorithmAssociationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_cleanroomsml.types.configured_model_algorithm_arn
    import capo_cleanroomsml.types.configured_model_algorithm_association_arn
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.privacy_configuration
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.tag_map
    import capo_cleanroomsml.types.uuid


class GetConfiguredModelAlgorithmAssociationResponse(TypedDict, closed=True):
    create_time: "datetime.datetime"
    """<p>The time at which the configured model algorithm association was created.</p>"""
    update_time: "datetime.datetime"
    """<p>The most recent time at which the configured model algorithm association was updated.</p>"""
    configured_model_algorithm_association_arn: "capo_cleanroomsml.types.configured_model_algorithm_association_arn.ConfiguredModelAlgorithmAssociationArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm association.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that created the configured model algorithm association.</p>"""
    collaboration_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The collaboration ID of the collaboration that contains the configured model algorithm association.</p>"""
    configured_model_algorithm_arn: "capo_cleanroomsml.types.configured_model_algorithm_arn.ConfiguredModelAlgorithmArn"
    """<p>The Amazon Resource Name (ARN) of the configured model algorithm that was associated to the collaboration.</p>"""
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the configured model algorithm association.</p>"""
    privacy_configuration: NotRequired[
        "capo_cleanroomsml.types.privacy_configuration.PrivacyConfiguration"
    ]
    """<p>The privacy configuration information for the configured model algorithm association.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the configured model algorithm association.</p>"""
    tags: NotRequired["capo_cleanroomsml.types.tag_map.TagMap"]
    """<p>The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.</p> <p>The following basic restrictions apply to tags:</p> <ul> <li> <p>Maximum number of tags per resource - 50.</p> </li> <li> <p>For each resource, each tag key must be unique, and each tag key can have only one value.</p> </li> <li> <p>Maximum key length - 128 Unicode characters in UTF-8.</p> </li> <li> <p>Maximum value length - 256 Unicode characters in UTF-8.</p> </li> <li> <p>If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: + - = . _ : / @.</p> </li> <li> <p>Tag keys and values are case sensitive.</p> </li> <li> <p>Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfiguredModelAlgorithmAssociationResponse) -> dict:
    out: dict = {}
    import capo_cleanroomsml.types._prelude.timestamp

    out["createTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["create_time"]
    )
    import capo_cleanroomsml.types._prelude.timestamp

    out["updateTime"] = capo_cleanroomsml.types._prelude.timestamp.serialize_json(
        value["update_time"]
    )
    out["configuredModelAlgorithmAssociationArn"] = value[
        "configured_model_algorithm_association_arn"
    ]
    out["membershipIdentifier"] = value["membership_identifier"]
    out["collaborationIdentifier"] = value["collaboration_identifier"]
    out["configuredModelAlgorithmArn"] = value["configured_model_algorithm_arn"]
    out["name"] = value["name"]
    if "privacy_configuration" in value:
        import capo_cleanroomsml.types.privacy_configuration

        out["privacyConfiguration"] = (
            capo_cleanroomsml.types.privacy_configuration.serialize_json(
                value["privacy_configuration"]
            )
        )
    if "description" in value:
        out["description"] = value["description"]
    if "tags" in value:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> GetConfiguredModelAlgorithmAssociationResponse:
    out: GetConfiguredModelAlgorithmAssociationResponse = {}  # type: ignore[typeddict-item]
    if "createTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["create_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["createTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.create_time required"
        )
    if "updateTime" in data:
        import capo_cleanroomsml.types._prelude.timestamp

        out["update_time"] = (
            capo_cleanroomsml.types._prelude.timestamp.deserialize_json(
                data["updateTime"]
            )
        )
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.update_time required"
        )
    if "configuredModelAlgorithmAssociationArn" in data:
        out["configured_model_algorithm_association_arn"] = data[
            "configuredModelAlgorithmAssociationArn"
        ]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.configured_model_algorithm_association_arn required"
        )
    if "membershipIdentifier" in data:
        out["membership_identifier"] = data["membershipIdentifier"]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.membership_identifier required"
        )
    if "collaborationIdentifier" in data:
        out["collaboration_identifier"] = data["collaborationIdentifier"]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.collaboration_identifier required"
        )
    if "configuredModelAlgorithmArn" in data:
        out["configured_model_algorithm_arn"] = data["configuredModelAlgorithmArn"]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.configured_model_algorithm_arn required"
        )
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError(
            "GetConfiguredModelAlgorithmAssociationResponse.name required"
        )
    if "privacyConfiguration" in data:
        import capo_cleanroomsml.types.privacy_configuration

        out["privacy_configuration"] = (
            capo_cleanroomsml.types.privacy_configuration.deserialize_json(
                data["privacyConfiguration"]
            )
        )
    if "description" in data:
        out["description"] = data["description"]
    if "tags" in data:
        import capo_cleanroomsml.types.tag_map

        out["tags"] = capo_cleanroomsml.types.tag_map.deserialize_json(data["tags"])
    return out
