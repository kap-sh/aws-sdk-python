"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#AnalysisRuleCriteria``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_accessanalyzer.types.account_ids_list
    import aws_sdk_accessanalyzer.types.tags_list


class AnalysisRuleCriteria(TypedDict):
    account_ids: NotRequired[
        "aws_sdk_accessanalyzer.types.account_ids_list.AccountIdsList"
    ]
    """<p>A list of Amazon Web Services account IDs to apply to the analysis rule criteria. The accounts cannot include the organization analyzer owner account. Account IDs can only be applied to the analysis rule criteria for organization-level analyzers. The list cannot include more than 2,000 account IDs.</p>"""
    resource_tags: NotRequired["aws_sdk_accessanalyzer.types.tags_list.TagsList"]
    """<p>An array of key-value pairs to match for your resources. You can use the set of Unicode letters, digits, whitespace, <code>_</code>, <code>.</code>, <code>/</code>, <code>=</code>, <code>+</code>, and <code>-</code>.</p> <p>For the tag key, you can specify a value that is 1 to 128 characters in length and cannot be prefixed with <code>aws:</code>.</p> <p>For the tag value, you can specify a value that is 0 to 256 characters in length. If the specified tag value is 0 characters, the rule is applied to all principals with the specified tag key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisRuleCriteria) -> dict:
    out: dict = {}
    if "account_ids" in value:
        import aws_sdk_accessanalyzer.types.account_ids_list

        out["accountIds"] = (
            aws_sdk_accessanalyzer.types.account_ids_list.serialize_json(
                value["account_ids"]
            )
        )
    if "resource_tags" in value:
        import aws_sdk_accessanalyzer.types.tags_list

        out["resourceTags"] = aws_sdk_accessanalyzer.types.tags_list.serialize_json(
            value["resource_tags"]
        )
    return out


def deserialize_json(data: dict) -> AnalysisRuleCriteria:
    out: AnalysisRuleCriteria = {}  # type: ignore[typeddict-item]
    if "accountIds" in data:
        import aws_sdk_accessanalyzer.types.account_ids_list

        out["account_ids"] = (
            aws_sdk_accessanalyzer.types.account_ids_list.deserialize_json(
                data["accountIds"]
            )
        )
    if "resourceTags" in data:
        import aws_sdk_accessanalyzer.types.tags_list

        out["resource_tags"] = aws_sdk_accessanalyzer.types.tags_list.deserialize_json(
            data["resourceTags"]
        )
    return out
