"""Generated from Smithy shape ``com.amazonaws.elasticache#ResetCacheParameterGroupMessage``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_elasticache.types.boolean
    import aws_sdk_elasticache.types.parameter_name_value_list
    import aws_sdk_elasticache.types.string


class ResetCacheParameterGroupMessage(TypedDict):
    cache_parameter_group_name: NotRequired["aws_sdk_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to reset.</p>"""
    reset_all_parameters: NotRequired["aws_sdk_elasticache.types.boolean.Boolean"]
    """<p>If <code>true</code>, all parameters in the cache parameter group are reset to their default values. If <code>false</code>, only the parameters listed by <code>ParameterNameValues</code> are reset to their default values.</p> <p>Valid values: <code>true</code> | <code>false</code> </p>"""
    parameter_name_values: NotRequired[
        "aws_sdk_elasticache.types.parameter_name_value_list.ParameterNameValueList"
    ]
    """<p>An array of parameter names to reset to their default values. If <code>ResetAllParameters</code> is <code>true</code>, do not use <code>ParameterNameValues</code>. If <code>ResetAllParameters</code> is <code>false</code>, you must specify the name of at least one parameter to reset.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ResetCacheParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{prefix}.CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "reset_all_parameters" in value:
        pairs.append(
            (
                f"{prefix}.ResetAllParameters",
                "true" if value["reset_all_parameters"] else "false",
            )
        )
    if "parameter_name_values" in value:
        import aws_sdk_elasticache.types.parameter_name_value_list

        aws_sdk_elasticache.types.parameter_name_value_list.serialize_query(
            value["parameter_name_values"], pairs, f"{prefix}.ParameterNameValues"
        )


def deserialize_query(el: Element) -> ResetCacheParameterGroupMessage:
    out: ResetCacheParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_reset_all_parameters = el.find("ResetAllParameters")
    if child_reset_all_parameters is not None:
        out["reset_all_parameters"] = (
            child_reset_all_parameters.text or ""
        ).lower() == "true"
    child_parameter_name_values = el.find("ParameterNameValues")
    if child_parameter_name_values is not None:
        import aws_sdk_elasticache.types.parameter_name_value_list

        out["parameter_name_values"] = (
            aws_sdk_elasticache.types.parameter_name_value_list.deserialize_query(
                child_parameter_name_values
            )
        )
    return out
