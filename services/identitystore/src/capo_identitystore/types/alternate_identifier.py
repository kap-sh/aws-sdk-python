"""Generated from Smithy shape ``com.amazonaws.identitystore#AlternateIdentifier``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_identitystore.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import capo_identitystore.types.external_id
    import capo_identitystore.types.unique_attribute


class _AlternateIdentifier_ExternalId(TypedDict, closed=True):
    ExternalId: "capo_identitystore.types.external_id.ExternalId"


class _AlternateIdentifier_UniqueAttribute(TypedDict, closed=True):
    UniqueAttribute: "capo_identitystore.types.unique_attribute.UniqueAttribute"


AlternateIdentifier: TypeAlias = (
    _AlternateIdentifier_ExternalId | _AlternateIdentifier_UniqueAttribute
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AlternateIdentifier) -> dict:
    if "ExternalId" in value:
        import capo_identitystore.types.external_id

        return {
            "ExternalId": capo_identitystore.types.external_id.serialize_aws_json_1_1(
                value["ExternalId"]
            )
        }
    elif "UniqueAttribute" in value:
        import capo_identitystore.types.unique_attribute

        return {
            "UniqueAttribute": capo_identitystore.types.unique_attribute.serialize_aws_json_1_1(
                value["UniqueAttribute"]
            )
        }
    else:
        raise SerializationError("AlternateIdentifier: no variant present")


def deserialize_aws_json_1_1(data: dict) -> AlternateIdentifier:
    if "ExternalId" in data:
        import capo_identitystore.types.external_id

        return {
            "ExternalId": capo_identitystore.types.external_id.deserialize_aws_json_1_1(
                data["ExternalId"]
            )
        }
    elif "UniqueAttribute" in data:
        import capo_identitystore.types.unique_attribute

        return {
            "UniqueAttribute": capo_identitystore.types.unique_attribute.deserialize_aws_json_1_1(
                data["UniqueAttribute"]
            )
        }
    else:
        raise DeserializationError("AlternateIdentifier: no recognized variant key")
