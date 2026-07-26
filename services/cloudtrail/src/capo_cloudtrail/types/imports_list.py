"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ImportsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cloudtrail.types.imports_list_item

ImportsList: TypeAlias = list["capo_cloudtrail.types.imports_list_item.ImportsListItem"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportsList) -> list:
    import capo_cloudtrail.types.imports_list_item

    out: list = []
    for item in value:
        out.append(capo_cloudtrail.types.imports_list_item.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImportsList:
    import capo_cloudtrail.types.imports_list_item

    out: ImportsList = []
    for item in data:
        out.append(
            capo_cloudtrail.types.imports_list_item.deserialize_aws_json_1_1(item)
        )
    return out
