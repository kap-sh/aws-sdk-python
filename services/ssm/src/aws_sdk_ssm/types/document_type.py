"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_ssm.errors import DeserializationError

DocumentType: TypeAlias = Literal[
    "Command",
    "Policy",
    "Automation",
    "Session",
    "Package",
    "ApplicationConfiguration",
    "ApplicationConfigurationSchema",
    "DeploymentStrategy",
    "ChangeCalendar",
    "Automation.ChangeTemplate",
    "ProblemAnalysis",
    "ProblemAnalysisTemplate",
    "CloudFormation",
    "ConformancePackTemplate",
    "QuickSetup",
    "ManualApprovalPolicy",
    "AutoApprovalPolicy",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Command",
        "Policy",
        "Automation",
        "Session",
        "Package",
        "ApplicationConfiguration",
        "ApplicationConfigurationSchema",
        "DeploymentStrategy",
        "ChangeCalendar",
        "Automation.ChangeTemplate",
        "ProblemAnalysis",
        "ProblemAnalysisTemplate",
        "CloudFormation",
        "ConformancePackTemplate",
        "QuickSetup",
        "ManualApprovalPolicy",
        "AutoApprovalPolicy",
    )
)


def serialize_aws_json_1_1(value: DocumentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DocumentType value: {data!r}")
    return cast(DocumentType, data)
