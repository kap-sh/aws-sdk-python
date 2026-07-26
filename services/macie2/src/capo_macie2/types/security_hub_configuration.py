"""Generated from Smithy shape ``com.amazonaws.macie2#SecurityHubConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_macie2.types.__boolean


class SecurityHubConfiguration(TypedDict, closed=True):
    publish_classification_findings: NotRequired[
        "capo_macie2.types.__boolean.__boolean"
    ]
    """<p>Specifies whether to publish sensitive data findings to Security Hub. If you set this value to true, Amazon Macie automatically publishes all sensitive data findings that weren't suppressed by a findings filter. The default value is false.</p>"""
    publish_policy_findings: NotRequired["capo_macie2.types.__boolean.__boolean"]
    """<p>Specifies whether to publish policy findings to Security Hub. If you set this value to true, Amazon Macie automatically publishes all new and updated policy findings that weren't suppressed by a findings filter. The default value is true.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SecurityHubConfiguration) -> dict:
    out: dict = {}
    if "publish_classification_findings" in value:
        out["publishClassificationFindings"] = value["publish_classification_findings"]
    if "publish_policy_findings" in value:
        out["publishPolicyFindings"] = value["publish_policy_findings"]
    return out


def deserialize_json(data: dict) -> SecurityHubConfiguration:
    out: SecurityHubConfiguration = {}  # type: ignore[typeddict-item]
    if "publishClassificationFindings" in data:
        out["publish_classification_findings"] = data["publishClassificationFindings"]
    if "publishPolicyFindings" in data:
        out["publish_policy_findings"] = data["publishPolicyFindings"]
    return out
