"""Generated from Smithy shape ``com.amazonaws.lexmodelbuildingservice#StartImportRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_lex_model_building_service.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lex_model_building_service.types.blob
    import aws_sdk_lex_model_building_service.types.merge_strategy
    import aws_sdk_lex_model_building_service.types.resource_type
    import aws_sdk_lex_model_building_service.types.tag_list


class StartImportRequest(TypedDict):
    payload: "aws_sdk_lex_model_building_service.types.blob.Blob"
    """<p>A zip archive in binary format. The archive should contain one file, a JSON file containing the resource to import. The resource should match the type specified in the <code>resourceType</code> field.</p>"""
    resource_type: "aws_sdk_lex_model_building_service.types.resource_type.ResourceType"
    """<p>Specifies the type of resource to export. Each resource also exports any resources that it depends on. </p> <ul> <li> <p>A bot exports dependent intents.</p> </li> <li> <p>An intent exports dependent slot types.</p> </li> </ul>"""
    merge_strategy: (
        "aws_sdk_lex_model_building_service.types.merge_strategy.MergeStrategy"
    )
    """<p>Specifies the action that the <code>StartImport</code> operation should take when there is an existing resource with the same name.</p> <ul> <li> <p>FAIL_ON_CONFLICT - The import operation is stopped on the first conflict between a resource in the import file and an existing resource. The name of the resource causing the conflict is in the <code>failureReason</code> field of the response to the <code>GetImport</code> operation.</p> <p>OVERWRITE_LATEST - The import operation proceeds even if there is a conflict with an existing resource. The $LASTEST version of the existing resource is overwritten with the data from the import file.</p> </li> </ul>"""
    tags: NotRequired["aws_sdk_lex_model_building_service.types.tag_list.TagList"]
    """<p>A list of tags to add to the imported bot. You can only add tags when you import a bot, you can't add tags to an intent or slot type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartImportRequest) -> dict:
    out: dict = {}
    import aws_sdk_lex_model_building_service.types.blob

    out["payload"] = aws_sdk_lex_model_building_service.types.blob.serialize_json(
        value["payload"]
    )
    import aws_sdk_lex_model_building_service.types.resource_type

    out["resourceType"] = (
        aws_sdk_lex_model_building_service.types.resource_type.serialize_json(
            value["resource_type"]
        )
    )
    import aws_sdk_lex_model_building_service.types.merge_strategy

    out["mergeStrategy"] = (
        aws_sdk_lex_model_building_service.types.merge_strategy.serialize_json(
            value["merge_strategy"]
        )
    )
    if "tags" in value:
        import aws_sdk_lex_model_building_service.types.tag_list

        out["tags"] = aws_sdk_lex_model_building_service.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> StartImportRequest:
    out: StartImportRequest = {}  # type: ignore[typeddict-item]
    if "payload" in data:
        import aws_sdk_lex_model_building_service.types.blob

        out["payload"] = aws_sdk_lex_model_building_service.types.blob.deserialize_json(
            data["payload"]
        )
    else:
        raise DeserializationError("StartImportRequest.payload required")
    if "resourceType" in data:
        import aws_sdk_lex_model_building_service.types.resource_type

        out["resource_type"] = (
            aws_sdk_lex_model_building_service.types.resource_type.deserialize_json(
                data["resourceType"]
            )
        )
    else:
        raise DeserializationError("StartImportRequest.resource_type required")
    if "mergeStrategy" in data:
        import aws_sdk_lex_model_building_service.types.merge_strategy

        out["merge_strategy"] = (
            aws_sdk_lex_model_building_service.types.merge_strategy.deserialize_json(
                data["mergeStrategy"]
            )
        )
    else:
        raise DeserializationError("StartImportRequest.merge_strategy required")
    if "tags" in data:
        import aws_sdk_lex_model_building_service.types.tag_list

        out["tags"] = (
            aws_sdk_lex_model_building_service.types.tag_list.deserialize_json(
                data["tags"]
            )
        )
    return out
