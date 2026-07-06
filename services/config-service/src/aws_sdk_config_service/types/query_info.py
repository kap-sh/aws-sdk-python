"""Generated from Smithy shape ``com.amazonaws.configservice#QueryInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_config_service.types.field_info_list


class QueryInfo(TypedDict, closed=True):
    select_fields: NotRequired[
        "aws_sdk_config_service.types.field_info_list.FieldInfoList"
    ]
    """<p>Returns a <code>FieldInfo</code> object.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryInfo) -> dict:
    out: dict = {}
    if "select_fields" in value:
        import aws_sdk_config_service.types.field_info_list

        out["SelectFields"] = (
            aws_sdk_config_service.types.field_info_list.serialize_aws_json_1_1(
                value["select_fields"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryInfo:
    out: QueryInfo = {}  # type: ignore[typeddict-item]
    if "SelectFields" in data:
        import aws_sdk_config_service.types.field_info_list

        out["select_fields"] = (
            aws_sdk_config_service.types.field_info_list.deserialize_aws_json_1_1(
                data["SelectFields"]
            )
        )
    return out
