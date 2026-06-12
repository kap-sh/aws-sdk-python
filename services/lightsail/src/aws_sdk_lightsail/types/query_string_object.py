"""Generated from Smithy shape ``com.amazonaws.lightsail#QueryStringObject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_lightsail.types.boolean
    import aws_sdk_lightsail.types.string_list


class QueryStringObject(TypedDict):
    option: NotRequired["aws_sdk_lightsail.types.boolean.boolean"]
    """<p>Indicates whether the distribution forwards and caches based on query strings.</p>"""
    query_strings_allow_list: NotRequired[
        "aws_sdk_lightsail.types.string_list.StringList"
    ]
    """<p>The specific query strings that the distribution forwards to the origin.</p> <p>Your distribution will cache content based on the specified query strings.</p> <p>If the <code>option</code> parameter is true, then your distribution forwards all query strings, regardless of what you specify using the <code>queryStringsAllowList</code> parameter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryStringObject) -> dict:
    out: dict = {}
    if "option" in value:
        out["option"] = value["option"]
    if "query_strings_allow_list" in value:
        import aws_sdk_lightsail.types.string_list

        out["queryStringsAllowList"] = (
            aws_sdk_lightsail.types.string_list.serialize_aws_json_1_1(
                value["query_strings_allow_list"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryStringObject:
    out: QueryStringObject = {}  # type: ignore[typeddict-item]
    if "option" in data:
        out["option"] = data["option"]
    if "queryStringsAllowList" in data:
        import aws_sdk_lightsail.types.string_list

        out["query_strings_allow_list"] = (
            aws_sdk_lightsail.types.string_list.deserialize_aws_json_1_1(
                data["queryStringsAllowList"]
            )
        )
    return out
