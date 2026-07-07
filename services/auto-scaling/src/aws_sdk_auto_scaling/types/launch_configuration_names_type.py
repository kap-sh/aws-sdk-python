"""Generated from Smithy shape ``com.amazonaws.autoscaling#LaunchConfigurationNamesType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_auto_scaling._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_auto_scaling.types.launch_configuration_names
    import aws_sdk_auto_scaling.types.max_records
    import aws_sdk_auto_scaling.types.xml_string


class LaunchConfigurationNamesType(TypedDict, closed=True):
    launch_configuration_names: NotRequired[
        "aws_sdk_auto_scaling.types.launch_configuration_names.LaunchConfigurationNames"
    ]
    """<p>The launch configuration names. If you omit this property, all launch configurations are described.</p> <p>Array Members: Maximum number of 50 items.</p>"""
    next_token: NotRequired["aws_sdk_auto_scaling.types.xml_string.XmlString"]
    """<p>The token for the next set of items to return. (You received this token from a previous call.)</p>"""
    max_records: NotRequired["aws_sdk_auto_scaling.types.max_records.MaxRecords"]
    """<p>The maximum number of items to return with this call. The default value is <code>50</code> and the maximum value is <code>100</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: LaunchConfigurationNamesType, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "launch_configuration_names" in value:
        import aws_sdk_auto_scaling.types.launch_configuration_names

        aws_sdk_auto_scaling.types.launch_configuration_names.serialize_query(
            value["launch_configuration_names"],
            pairs,
            f"{prefix}.LaunchConfigurationNames",
        )
    if "next_token" in value:
        pairs.append((f"{prefix}.NextToken", str(value["next_token"])))
    if "max_records" in value:
        pairs.append((f"{prefix}.MaxRecords", str(value["max_records"])))


def deserialize_query(el: Element) -> LaunchConfigurationNamesType:
    out: LaunchConfigurationNamesType = {}  # type: ignore[typeddict-item]
    child_launch_configuration_names = el.find("LaunchConfigurationNames")
    if child_launch_configuration_names is not None:
        import aws_sdk_auto_scaling.types.launch_configuration_names

        out["launch_configuration_names"] = (
            aws_sdk_auto_scaling.types.launch_configuration_names.deserialize_query(
                child_launch_configuration_names
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    child_max_records = el.find("MaxRecords")
    if child_max_records is not None:
        out["max_records"] = int(child_max_records.text or "")
    return out
