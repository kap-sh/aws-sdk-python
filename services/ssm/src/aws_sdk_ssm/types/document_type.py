"""Generated from Smithy shape ``com.amazonaws.ssm#DocumentType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: DocumentType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DocumentType:
    return cast(DocumentType, data)
