"""Generated from Smithy shape ``com.amazonaws.ses#ReputationOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_ses._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_ses.types.enabled
    import aws_sdk_ses.types.last_fresh_start


class ReputationOptions(TypedDict, closed=True):
    sending_enabled: "aws_sdk_ses.types.enabled.Enabled"
    """<p>Describes whether email sending is enabled or disabled for the configuration set. If the value is <code>true</code>, then Amazon SES sends emails that use the configuration set. If the value is <code>false</code>, Amazon SES does not send emails that use the configuration set. The default value is <code>true</code>. You can change this setting using <a>UpdateConfigurationSetSendingEnabled</a>.</p>"""
    reputation_metrics_enabled: "aws_sdk_ses.types.enabled.Enabled"
    """<p>Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.</p> <p>If the value is <code>true</code>, reputation metrics are published. If the value is <code>false</code>, reputation metrics are not published. The default value is <code>false</code>.</p>"""
    last_fresh_start: NotRequired["aws_sdk_ses.types.last_fresh_start.LastFreshStart"]
    """<p>The date and time at which the reputation metrics for the configuration set were last reset. Resetting these metrics is known as a <i>fresh start</i>.</p> <p>When you disable email sending for a configuration set using <a>UpdateConfigurationSetSendingEnabled</a> and later re-enable it, the reputation metrics for the configuration set (but not for the entire Amazon SES account) are reset.</p> <p>If email sending for the configuration set has never been disabled and later re-enabled, the value of this attribute is <code>null</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: ReputationOptions, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append(
        (
            f"{prefix}.SendingEnabled",
            "true" if value.get("sending_enabled", False) else "false",
        )
    )
    pairs.append(
        (
            f"{prefix}.ReputationMetricsEnabled",
            "true" if value.get("reputation_metrics_enabled", False) else "false",
        )
    )
    if "last_fresh_start" in value:
        import aws_sdk_ses.types.last_fresh_start

        aws_sdk_ses.types.last_fresh_start.serialize_query(
            value["last_fresh_start"], pairs, f"{prefix}.LastFreshStart"
        )


def deserialize_query(el: Element) -> ReputationOptions:
    out: ReputationOptions = {}  # type: ignore[typeddict-item]
    child_sending_enabled = el.find("SendingEnabled")
    if child_sending_enabled is not None:
        out["sending_enabled"] = (child_sending_enabled.text or "").lower() == "true"
    else:
        out["sending_enabled"] = False
    child_reputation_metrics_enabled = el.find("ReputationMetricsEnabled")
    if child_reputation_metrics_enabled is not None:
        out["reputation_metrics_enabled"] = (
            child_reputation_metrics_enabled.text or ""
        ).lower() == "true"
    else:
        out["reputation_metrics_enabled"] = False
    child_last_fresh_start = el.find("LastFreshStart")
    if child_last_fresh_start is not None:
        import aws_sdk_ses.types.last_fresh_start

        out["last_fresh_start"] = aws_sdk_ses.types.last_fresh_start.deserialize_query(
            child_last_fresh_start
        )
    return out
