"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#PlatformFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.platform_filter_operator
    import capo_elastic_beanstalk.types.platform_filter_type
    import capo_elastic_beanstalk.types.platform_filter_value_list


class PlatformFilter(TypedDict, closed=True):
    type: NotRequired[
        "capo_elastic_beanstalk.types.platform_filter_type.PlatformFilterType"
    ]
    """<p>The platform version attribute to which the filter values are applied.</p> <p>Valid values: <code>PlatformName</code> | <code>PlatformVersion</code> | <code>PlatformStatus</code> | <code>PlatformBranchName</code> | <code>PlatformLifecycleState</code> | <code>PlatformOwner</code> | <code>SupportedTier</code> | <code>SupportedAddon</code> | <code>ProgrammingLanguageName</code> | <code>OperatingSystemName</code> </p>"""
    operator: NotRequired[
        "capo_elastic_beanstalk.types.platform_filter_operator.PlatformFilterOperator"
    ]
    """<p>The operator to apply to the <code>Type</code> with each of the <code>Values</code>.</p> <p>Valid values: <code>=</code> | <code>!=</code> | <code><</code> | <code><=</code> | <code>></code> | <code>>=</code> | <code>contains</code> | <code>begins_with</code> | <code>ends_with</code> </p>"""
    values: NotRequired[
        "capo_elastic_beanstalk.types.platform_filter_value_list.PlatformFilterValueList"
    ]
    """<p>The list of values applied to the filtering platform version attribute. Only one value is supported for all current operators.</p> <p>The following list shows valid filter values for some filter attributes.</p> <ul> <li> <p> <code>PlatformStatus</code>: <code>Creating</code> | <code>Failed</code> | <code>Ready</code> | <code>Deleting</code> | <code>Deleted</code> </p> </li> <li> <p> <code>PlatformLifecycleState</code>: <code>recommended</code> </p> </li> <li> <p> <code>SupportedTier</code>: <code>WebServer/Standard</code> | <code>Worker/SQS/HTTP</code> </p> </li> <li> <p> <code>SupportedAddon</code>: <code>Log/S3</code> | <code>Monitoring/Healthd</code> | <code>WorkerDaemon/SQSD</code> </p> </li> </ul>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: PlatformFilter, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "type" in value:
        pairs.append((f"{key_prefix}Type", str(value["type"])))
    if "operator" in value:
        pairs.append((f"{key_prefix}Operator", str(value["operator"])))
    if "values" in value:
        import capo_elastic_beanstalk.types.platform_filter_value_list

        capo_elastic_beanstalk.types.platform_filter_value_list.serialize_query(
            value["values"], pairs, f"{key_prefix}Values"
        )


def deserialize_query(el: Element) -> PlatformFilter:
    out: PlatformFilter = {}  # type: ignore[typeddict-item]
    child_type = el.find("Type")
    if child_type is not None:
        out["type"] = str(child_type.text or "")
    child_operator = el.find("Operator")
    if child_operator is not None:
        out["operator"] = str(child_operator.text or "")
    child_values = el.find("Values")
    if child_values is not None:
        import capo_elastic_beanstalk.types.platform_filter_value_list

        out["values"] = (
            capo_elastic_beanstalk.types.platform_filter_value_list.deserialize_query(
                child_values
            )
        )
    return out
