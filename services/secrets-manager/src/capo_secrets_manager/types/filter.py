"""Generated from Smithy shape ``com.amazonaws.secretsmanager#Filter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_secrets_manager.types.filter_name_string_type
    import capo_secrets_manager.types.filter_values_string_list


class Filter(TypedDict, closed=True):
    key: NotRequired[
        "capo_secrets_manager.types.filter_name_string_type.FilterNameStringType"
    ]
    """<p>The following are keys you can use:</p> <ul> <li> <p> <b>description</b>: Prefix match, not case-sensitive.</p> </li> <li> <p> <b>name</b>: Prefix match, case-sensitive.</p> </li> <li> <p> <b>tag-key</b>: Prefix match, case-sensitive.</p> </li> <li> <p> <b>tag-value</b>: Prefix match, case-sensitive.</p> </li> <li> <p> <b>primary-region</b>: Prefix match, case-sensitive.</p> </li> <li> <p> <b>owning-service</b>: Prefix match, case-sensitive.</p> </li> <li> <p> <b>all</b>: Breaks the filter value string into words and then searches all attributes for matches. Not case-sensitive.</p> </li> </ul>"""
    values: NotRequired[
        "capo_secrets_manager.types.filter_values_string_list.FilterValuesStringList"
    ]
    """<p>The keyword to filter for.</p> <p>You can prefix your search value with an exclamation mark (<code>!</code>) in order to perform negation filters. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Filter) -> dict:
    out: dict = {}
    if "key" in value:
        import capo_secrets_manager.types.filter_name_string_type

        out["Key"] = (
            capo_secrets_manager.types.filter_name_string_type.serialize_aws_json_1_1(
                value["key"]
            )
        )
    if "values" in value:
        import capo_secrets_manager.types.filter_values_string_list

        out["Values"] = (
            capo_secrets_manager.types.filter_values_string_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Filter:
    out: Filter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_secrets_manager.types.filter_name_string_type

        out["key"] = (
            capo_secrets_manager.types.filter_name_string_type.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    if data.get("Values") is not None:
        import capo_secrets_manager.types.filter_values_string_list

        out["values"] = (
            capo_secrets_manager.types.filter_values_string_list.deserialize_aws_json_1_1(
                data["Values"]
            )
        )
    return out
