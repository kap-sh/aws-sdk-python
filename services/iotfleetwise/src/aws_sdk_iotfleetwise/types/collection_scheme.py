"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CollectionScheme``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_iotfleetwise.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.condition_based_collection_scheme
    import aws_sdk_iotfleetwise.types.time_based_collection_scheme


class _CollectionScheme_timeBasedCollectionScheme(TypedDict, closed=True):
    timeBasedCollectionScheme: "aws_sdk_iotfleetwise.types.time_based_collection_scheme.TimeBasedCollectionScheme"


class _CollectionScheme_conditionBasedCollectionScheme(TypedDict, closed=True):
    conditionBasedCollectionScheme: "aws_sdk_iotfleetwise.types.condition_based_collection_scheme.ConditionBasedCollectionScheme"


CollectionScheme: TypeAlias = (
    _CollectionScheme_timeBasedCollectionScheme
    | _CollectionScheme_conditionBasedCollectionScheme
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CollectionScheme) -> dict:
    if "timeBasedCollectionScheme" in value:
        import aws_sdk_iotfleetwise.types.time_based_collection_scheme

        return {
            "timeBasedCollectionScheme": aws_sdk_iotfleetwise.types.time_based_collection_scheme.serialize_aws_json_1_0(
                value["timeBasedCollectionScheme"]
            )
        }
    elif "conditionBasedCollectionScheme" in value:
        import aws_sdk_iotfleetwise.types.condition_based_collection_scheme

        return {
            "conditionBasedCollectionScheme": aws_sdk_iotfleetwise.types.condition_based_collection_scheme.serialize_aws_json_1_0(
                value["conditionBasedCollectionScheme"]
            )
        }
    else:
        raise SerializationError("CollectionScheme: no variant present")


def deserialize_aws_json_1_0(data: dict) -> CollectionScheme:
    if "timeBasedCollectionScheme" in data:
        import aws_sdk_iotfleetwise.types.time_based_collection_scheme

        return {
            "timeBasedCollectionScheme": aws_sdk_iotfleetwise.types.time_based_collection_scheme.deserialize_aws_json_1_0(
                data["timeBasedCollectionScheme"]
            )
        }
    elif "conditionBasedCollectionScheme" in data:
        import aws_sdk_iotfleetwise.types.condition_based_collection_scheme

        return {
            "conditionBasedCollectionScheme": aws_sdk_iotfleetwise.types.condition_based_collection_scheme.deserialize_aws_json_1_0(
                data["conditionBasedCollectionScheme"]
            )
        }
    else:
        raise DeserializationError("CollectionScheme: no recognized variant key")
