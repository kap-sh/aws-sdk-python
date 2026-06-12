"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#CreateAnalyzerRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_accessanalyzer.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.analyzer_configuration
    import aws_sdk_accessanalyzer.types.analyzer_name
    import aws_sdk_accessanalyzer.types.inline_archive_rules_list
    import aws_sdk_accessanalyzer.types.tags_map
    import aws_sdk_accessanalyzer.types.type


class CreateAnalyzerRequest(TypedDict):
    analyzer_name: "aws_sdk_accessanalyzer.types.analyzer_name.AnalyzerName"
    """<p>The name of the analyzer to create.</p>"""
    type: "aws_sdk_accessanalyzer.types.type.Type"
    """<p>The type of analyzer to create. You can create only one analyzer per account per Region. You can create up to 5 analyzers per organization per Region.</p>"""
    archive_rules: NotRequired[
        "aws_sdk_accessanalyzer.types.inline_archive_rules_list.InlineArchiveRulesList"
    ]
    """<p>Specifies the archive rules to add for the analyzer. Archive rules automatically archive findings that meet the criteria you define for the rule.</p>"""
    tags: NotRequired["aws_sdk_accessanalyzer.types.tags_map.TagsMap"]
    """<p>An array of key-value pairs to apply to the analyzer. You can use the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>For the tag value, you can specify a value that is 0 to 256 characters in length.</p>"""
    client_token: NotRequired["str"]
    """<p>A client token.</p>"""
    configuration: NotRequired[
        "aws_sdk_accessanalyzer.types.analyzer_configuration.AnalyzerConfiguration"
    ]
    """<p>Specifies the configuration of the analyzer. If the analyzer is an unused access analyzer, the specified scope of unused access is used for the configuration. If the analyzer is an internal access analyzer, the specified internal access analysis rules are used for the configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAnalyzerRequest) -> dict:
    out: dict = {}
    out["analyzerName"] = value["analyzer_name"]
    out["type"] = value["type"]
    if "archive_rules" in value:
        import aws_sdk_accessanalyzer.types.inline_archive_rules_list

        out["archiveRules"] = (
            aws_sdk_accessanalyzer.types.inline_archive_rules_list.serialize_json(
                value["archive_rules"]
            )
        )
    if "tags" in value:
        import aws_sdk_accessanalyzer.types.tags_map

        out["tags"] = aws_sdk_accessanalyzer.types.tags_map.serialize_json(
            value["tags"]
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "configuration" in value:
        import aws_sdk_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            aws_sdk_accessanalyzer.types.analyzer_configuration.serialize_json(
                value["configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateAnalyzerRequest:
    out: CreateAnalyzerRequest = {}  # type: ignore[typeddict-item]
    if "analyzerName" in data:
        out["analyzer_name"] = data["analyzerName"]
    else:
        raise DeserializationError("CreateAnalyzerRequest.analyzer_name required")
    if "type" in data:
        out["type"] = data["type"]
    else:
        raise DeserializationError("CreateAnalyzerRequest.type required")
    if "archiveRules" in data:
        import aws_sdk_accessanalyzer.types.inline_archive_rules_list

        out["archive_rules"] = (
            aws_sdk_accessanalyzer.types.inline_archive_rules_list.deserialize_json(
                data["archiveRules"]
            )
        )
    if "tags" in data:
        import aws_sdk_accessanalyzer.types.tags_map

        out["tags"] = aws_sdk_accessanalyzer.types.tags_map.deserialize_json(
            data["tags"]
        )
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "configuration" in data:
        import aws_sdk_accessanalyzer.types.analyzer_configuration

        out["configuration"] = (
            aws_sdk_accessanalyzer.types.analyzer_configuration.deserialize_json(
                data["configuration"]
            )
        )
    return out
