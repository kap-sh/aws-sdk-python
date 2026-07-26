"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobDeploymentInstanceType``."""

from typing import Literal, TypeAlias, cast

OptimizationJobDeploymentInstanceType: TypeAlias = Literal[
    "ml.p4d.24xlarge",
    "ml.p4de.24xlarge",
    "ml.p5.48xlarge",
    "ml.p5e.48xlarge",
    "ml.p5en.48xlarge",
    "ml.g4dn.xlarge",
    "ml.g4dn.2xlarge",
    "ml.g4dn.4xlarge",
    "ml.g4dn.8xlarge",
    "ml.g4dn.12xlarge",
    "ml.g4dn.16xlarge",
    "ml.g5.xlarge",
    "ml.g5.2xlarge",
    "ml.g5.4xlarge",
    "ml.g5.8xlarge",
    "ml.g5.12xlarge",
    "ml.g5.16xlarge",
    "ml.g5.24xlarge",
    "ml.g5.48xlarge",
    "ml.g6.xlarge",
    "ml.g6.2xlarge",
    "ml.g6.4xlarge",
    "ml.g6.8xlarge",
    "ml.g6.12xlarge",
    "ml.g6.16xlarge",
    "ml.g6.24xlarge",
    "ml.g6.48xlarge",
    "ml.g6e.xlarge",
    "ml.g6e.2xlarge",
    "ml.g6e.4xlarge",
    "ml.g6e.8xlarge",
    "ml.g6e.12xlarge",
    "ml.g6e.16xlarge",
    "ml.g6e.24xlarge",
    "ml.g6e.48xlarge",
    "ml.inf2.xlarge",
    "ml.inf2.8xlarge",
    "ml.inf2.24xlarge",
    "ml.inf2.48xlarge",
    "ml.trn1.2xlarge",
    "ml.trn1.32xlarge",
    "ml.trn1n.32xlarge",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobDeploymentInstanceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OptimizationJobDeploymentInstanceType:
    return cast(OptimizationJobDeploymentInstanceType, data)
