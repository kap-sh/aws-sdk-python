"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseAssetRule``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_license_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_license_manager.types.rule_statement


class LicenseAssetRule(TypedDict, closed=True):
    rule_statement: "capo_license_manager.types.rule_statement.RuleStatement"
    """<p>Rule statement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseAssetRule) -> dict:
    out: dict = {}
    import capo_license_manager.types.rule_statement

    out["RuleStatement"] = (
        capo_license_manager.types.rule_statement.serialize_aws_json_1_1(
            value["rule_statement"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseAssetRule:
    out: LicenseAssetRule = {}  # type: ignore[typeddict-item]
    if "RuleStatement" in data:
        import capo_license_manager.types.rule_statement

        out["rule_statement"] = (
            capo_license_manager.types.rule_statement.deserialize_aws_json_1_1(
                data["RuleStatement"]
            )
        )
    else:
        raise DeserializationError("LicenseAssetRule.rule_statement required")
    return out
