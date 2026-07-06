"""Generated from Smithy shape ``com.amazonaws.bedrock#RequestMetadataFilters``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_bedrock.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.request_metadata_filters_list
    import aws_sdk_bedrock.types.request_metadata_map


class _RequestMetadataFilters_equals(TypedDict, closed=True):
    equals: "aws_sdk_bedrock.types.request_metadata_map.RequestMetadataMap"


class _RequestMetadataFilters_notEquals(TypedDict, closed=True):
    notEquals: "aws_sdk_bedrock.types.request_metadata_map.RequestMetadataMap"


class _RequestMetadataFilters_andAll(TypedDict, closed=True):
    andAll: (
        "aws_sdk_bedrock.types.request_metadata_filters_list.RequestMetadataFiltersList"
    )


class _RequestMetadataFilters_orAll(TypedDict, closed=True):
    orAll: (
        "aws_sdk_bedrock.types.request_metadata_filters_list.RequestMetadataFiltersList"
    )


RequestMetadataFilters: TypeAlias = (
    _RequestMetadataFilters_equals
    | _RequestMetadataFilters_notEquals
    | _RequestMetadataFilters_andAll
    | _RequestMetadataFilters_orAll
)


# --- restJson1 ser/de ---
def serialize_json(value: RequestMetadataFilters) -> dict:
    if "equals" in value:
        import aws_sdk_bedrock.types.request_metadata_map

        return {
            "equals": aws_sdk_bedrock.types.request_metadata_map.serialize_json(
                value["equals"]
            )
        }
    elif "notEquals" in value:
        import aws_sdk_bedrock.types.request_metadata_map

        return {
            "notEquals": aws_sdk_bedrock.types.request_metadata_map.serialize_json(
                value["notEquals"]
            )
        }
    elif "andAll" in value:
        import aws_sdk_bedrock.types.request_metadata_filters_list

        return {
            "andAll": aws_sdk_bedrock.types.request_metadata_filters_list.serialize_json(
                value["andAll"]
            )
        }
    elif "orAll" in value:
        import aws_sdk_bedrock.types.request_metadata_filters_list

        return {
            "orAll": aws_sdk_bedrock.types.request_metadata_filters_list.serialize_json(
                value["orAll"]
            )
        }
    else:
        raise SerializationError("RequestMetadataFilters: no variant present")


def deserialize_json(data: dict) -> RequestMetadataFilters:
    if "equals" in data:
        import aws_sdk_bedrock.types.request_metadata_map

        return {
            "equals": aws_sdk_bedrock.types.request_metadata_map.deserialize_json(
                data["equals"]
            )
        }
    elif "notEquals" in data:
        import aws_sdk_bedrock.types.request_metadata_map

        return {
            "notEquals": aws_sdk_bedrock.types.request_metadata_map.deserialize_json(
                data["notEquals"]
            )
        }
    elif "andAll" in data:
        import aws_sdk_bedrock.types.request_metadata_filters_list

        return {
            "andAll": aws_sdk_bedrock.types.request_metadata_filters_list.deserialize_json(
                data["andAll"]
            )
        }
    elif "orAll" in data:
        import aws_sdk_bedrock.types.request_metadata_filters_list

        return {
            "orAll": aws_sdk_bedrock.types.request_metadata_filters_list.deserialize_json(
                data["orAll"]
            )
        }
    else:
        raise DeserializationError("RequestMetadataFilters: no recognized variant key")
