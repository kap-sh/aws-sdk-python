"""Generated from Smithy shape ``com.amazonaws.elasticbeanstalk#ConfigurationOptionDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_elastic_beanstalk._protocol.xml import Element

if TYPE_CHECKING:
    import capo_elastic_beanstalk.types.configuration_option_default_value
    import capo_elastic_beanstalk.types.configuration_option_name
    import capo_elastic_beanstalk.types.configuration_option_possible_values
    import capo_elastic_beanstalk.types.configuration_option_severity
    import capo_elastic_beanstalk.types.configuration_option_value_type
    import capo_elastic_beanstalk.types.option_namespace
    import capo_elastic_beanstalk.types.option_restriction_max_length
    import capo_elastic_beanstalk.types.option_restriction_max_value
    import capo_elastic_beanstalk.types.option_restriction_min_value
    import capo_elastic_beanstalk.types.option_restriction_regex
    import capo_elastic_beanstalk.types.user_defined_option


class ConfigurationOptionDescription(TypedDict, closed=True):
    namespace: NotRequired[
        "capo_elastic_beanstalk.types.option_namespace.OptionNamespace"
    ]
    """<p>A unique namespace identifying the option's associated AWS resource.</p>"""
    name: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_name.ConfigurationOptionName"
    ]
    """<p>The name of the configuration option.</p>"""
    default_value: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_default_value.ConfigurationOptionDefaultValue"
    ]
    """<p>The default value for this configuration option.</p>"""
    change_severity: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_severity.ConfigurationOptionSeverity"
    ]
    """<p>An indication of which action is required if the value for this configuration option changes:</p> <ul> <li> <p> <code>NoInterruption</code> : There is no interruption to the environment or application availability.</p> </li> <li> <p> <code>RestartEnvironment</code> : The environment is entirely restarted, all AWS resources are deleted and recreated, and the environment is unavailable during the process.</p> </li> <li> <p> <code>RestartApplicationServer</code> : The environment is available the entire time. However, a short application outage occurs when the application servers on the running Amazon EC2 instances are restarted.</p> </li> </ul>"""
    user_defined: NotRequired[
        "capo_elastic_beanstalk.types.user_defined_option.UserDefinedOption"
    ]
    """<p>An indication of whether the user defined this configuration option:</p> <ul> <li> <p> <code>true</code> : This configuration option was defined by the user. It is a valid choice for specifying if this as an <code>Option to Remove</code> when updating configuration settings. </p> </li> <li> <p> <code>false</code> : This configuration was not defined by the user.</p> </li> </ul> <p> Constraint: You can remove only <code>UserDefined</code> options from a configuration. </p> <p> Valid Values: <code>true</code> | <code>false</code> </p>"""
    value_type: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_value_type.ConfigurationOptionValueType"
    ]
    """<p>An indication of which type of values this option has and whether it is allowable to select one or more than one of the possible values:</p> <ul> <li> <p> <code>Scalar</code> : Values for this option are a single selection from the possible values, or an unformatted string, or numeric value governed by the <code>MIN/MAX/Regex</code> constraints.</p> </li> <li> <p> <code>List</code> : Values for this option are multiple selections from the possible values.</p> </li> <li> <p> <code>Boolean</code> : Values for this option are either <code>true</code> or <code>false</code> .</p> </li> <li> <p> <code>Json</code> : Values for this option are a JSON representation of a <code>ConfigDocument</code>.</p> </li> </ul>"""
    value_options: NotRequired[
        "capo_elastic_beanstalk.types.configuration_option_possible_values.ConfigurationOptionPossibleValues"
    ]
    """<p>If specified, values for the configuration option are selected from this list.</p>"""
    min_value: NotRequired[
        "capo_elastic_beanstalk.types.option_restriction_min_value.OptionRestrictionMinValue"
    ]
    """<p>If specified, the configuration option must be a numeric value greater than this value.</p>"""
    max_value: NotRequired[
        "capo_elastic_beanstalk.types.option_restriction_max_value.OptionRestrictionMaxValue"
    ]
    """<p>If specified, the configuration option must be a numeric value less than this value.</p>"""
    max_length: NotRequired[
        "capo_elastic_beanstalk.types.option_restriction_max_length.OptionRestrictionMaxLength"
    ]
    """<p>If specified, the configuration option must be a string value no longer than this value.</p>"""
    regex: NotRequired[
        "capo_elastic_beanstalk.types.option_restriction_regex.OptionRestrictionRegex"
    ]
    """<p>If specified, the configuration option must be a string value that satisfies this regular expression.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ConfigurationOptionDescription, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "namespace" in value:
        pairs.append((f"{key_prefix}Namespace", str(value["namespace"])))
    if "name" in value:
        pairs.append((f"{key_prefix}Name", str(value["name"])))
    if "default_value" in value:
        pairs.append((f"{key_prefix}DefaultValue", str(value["default_value"])))
    if "change_severity" in value:
        pairs.append((f"{key_prefix}ChangeSeverity", str(value["change_severity"])))
    if "user_defined" in value:
        pairs.append(
            (f"{key_prefix}UserDefined", "true" if value["user_defined"] else "false")
        )
    if "value_type" in value:
        import capo_elastic_beanstalk.types.configuration_option_value_type

        capo_elastic_beanstalk.types.configuration_option_value_type.serialize_query(
            value["value_type"], pairs, f"{key_prefix}ValueType"
        )
    if "value_options" in value:
        import capo_elastic_beanstalk.types.configuration_option_possible_values

        capo_elastic_beanstalk.types.configuration_option_possible_values.serialize_query(
            value["value_options"], pairs, f"{key_prefix}ValueOptions"
        )
    if "min_value" in value:
        pairs.append((f"{key_prefix}MinValue", str(value["min_value"])))
    if "max_value" in value:
        pairs.append((f"{key_prefix}MaxValue", str(value["max_value"])))
    if "max_length" in value:
        pairs.append((f"{key_prefix}MaxLength", str(value["max_length"])))
    if "regex" in value:
        import capo_elastic_beanstalk.types.option_restriction_regex

        capo_elastic_beanstalk.types.option_restriction_regex.serialize_query(
            value["regex"], pairs, f"{key_prefix}Regex"
        )


def deserialize_query(el: Element) -> ConfigurationOptionDescription:
    out: ConfigurationOptionDescription = {}  # type: ignore[typeddict-item]
    child_namespace = el.find("Namespace")
    if child_namespace is not None:
        out["namespace"] = str(child_namespace.text or "")
    child_name = el.find("Name")
    if child_name is not None:
        out["name"] = str(child_name.text or "")
    child_default_value = el.find("DefaultValue")
    if child_default_value is not None:
        out["default_value"] = str(child_default_value.text or "")
    child_change_severity = el.find("ChangeSeverity")
    if child_change_severity is not None:
        out["change_severity"] = str(child_change_severity.text or "")
    child_user_defined = el.find("UserDefined")
    if child_user_defined is not None:
        out["user_defined"] = (child_user_defined.text or "").lower() == "true"
    child_value_type = el.find("ValueType")
    if child_value_type is not None:
        import capo_elastic_beanstalk.types.configuration_option_value_type

        out["value_type"] = (
            capo_elastic_beanstalk.types.configuration_option_value_type.deserialize_query(
                child_value_type
            )
        )
    child_value_options = el.find("ValueOptions")
    if child_value_options is not None:
        import capo_elastic_beanstalk.types.configuration_option_possible_values

        out["value_options"] = (
            capo_elastic_beanstalk.types.configuration_option_possible_values.deserialize_query(
                child_value_options
            )
        )
    child_min_value = el.find("MinValue")
    if child_min_value is not None:
        out["min_value"] = int(child_min_value.text or "")
    child_max_value = el.find("MaxValue")
    if child_max_value is not None:
        out["max_value"] = int(child_max_value.text or "")
    child_max_length = el.find("MaxLength")
    if child_max_length is not None:
        out["max_length"] = int(child_max_length.text or "")
    child_regex = el.find("Regex")
    if child_regex is not None:
        import capo_elastic_beanstalk.types.option_restriction_regex

        out["regex"] = (
            capo_elastic_beanstalk.types.option_restriction_regex.deserialize_query(
                child_regex
            )
        )
    return out
