"""Generated from Smithy shape ``com.amazonaws.elasticache#ModifyCacheParameterGroupMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elasticache._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elasticache.types.parameter_name_value_list
    import capo_elasticache.types.string


class ModifyCacheParameterGroupMessage(TypedDict, closed=True):
    cache_parameter_group_name: NotRequired["capo_elasticache.types.string.String"]
    """<p>The name of the cache parameter group to modify.</p>"""
    parameter_name_values: NotRequired[
        "capo_elasticache.types.parameter_name_value_list.ParameterNameValueList"
    ]
    """<p>An array of parameter names and values for the parameter update. You must supply at least one parameter name and value; subsequent arguments are optional. A maximum of 20 parameters may be modified per request.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ModifyCacheParameterGroupMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "cache_parameter_group_name" in value:
        pairs.append(
            (
                f"{key_prefix}CacheParameterGroupName",
                str(value["cache_parameter_group_name"]),
            )
        )
    if "parameter_name_values" in value:
        import capo_elasticache.types.parameter_name_value_list

        capo_elasticache.types.parameter_name_value_list.serialize_query(
            value["parameter_name_values"], pairs, f"{key_prefix}ParameterNameValues"
        )


def deserialize_query(el: Element) -> ModifyCacheParameterGroupMessage:
    out: ModifyCacheParameterGroupMessage = {}  # type: ignore[typeddict-item]
    child_cache_parameter_group_name = el.find("CacheParameterGroupName")
    if child_cache_parameter_group_name is not None:
        out["cache_parameter_group_name"] = str(
            child_cache_parameter_group_name.text or ""
        )
    child_parameter_name_values = el.find("ParameterNameValues")
    if child_parameter_name_values is not None:
        import capo_elasticache.types.parameter_name_value_list

        out["parameter_name_values"] = (
            capo_elasticache.types.parameter_name_value_list.deserialize_query(
                child_parameter_name_values
            )
        )
    return out
