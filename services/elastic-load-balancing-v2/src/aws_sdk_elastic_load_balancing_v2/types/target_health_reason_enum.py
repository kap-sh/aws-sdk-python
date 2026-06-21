"""Generated from Smithy shape ``com.amazonaws.elasticloadbalancingv2#TargetHealthReasonEnum``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_elastic_load_balancing_v2._protocol.xml import Element

TargetHealthReasonEnum: TypeAlias = Literal[
    "Elb.RegistrationInProgress",
    "Elb.InitialHealthChecking",
    "Target.ResponseCodeMismatch",
    "Target.Timeout",
    "Target.FailedHealthChecks",
    "Target.NotRegistered",
    "Target.NotInUse",
    "Target.DeregistrationInProgress",
    "Target.InvalidState",
    "Target.IpUnusable",
    "Target.HealthCheckDisabled",
    "Elb.InternalError",
]


# --- awsQuery ser/de ---
def to_query_text(value: TargetHealthReasonEnum) -> str:
    return value


def from_query_text(text: str) -> TargetHealthReasonEnum:
    return cast(TargetHealthReasonEnum, text)


def serialize_query(
    value: TargetHealthReasonEnum, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((prefix, to_query_text(value)))


def deserialize_query(el: Element) -> TargetHealthReasonEnum:
    return from_query_text(el.text or "")
