"""Generated from Smithy shape ``com.amazonaws.sagemaker#MIGProfileType``."""

from typing import Literal, TypeAlias, cast

MIGProfileType: TypeAlias = Literal[
    "mig-1g.5gb",
    "mig-1g.10gb",
    "mig-1g.18gb",
    "mig-1g.20gb",
    "mig-1g.23gb",
    "mig-1g.35gb",
    "mig-1g.45gb",
    "mig-1g.47gb",
    "mig-2g.10gb",
    "mig-2g.20gb",
    "mig-2g.35gb",
    "mig-2g.45gb",
    "mig-2g.47gb",
    "mig-3g.20gb",
    "mig-3g.40gb",
    "mig-3g.71gb",
    "mig-3g.90gb",
    "mig-3g.93gb",
    "mig-4g.20gb",
    "mig-4g.40gb",
    "mig-4g.71gb",
    "mig-4g.90gb",
    "mig-4g.93gb",
    "mig-7g.40gb",
    "mig-7g.80gb",
    "mig-7g.141gb",
    "mig-7g.180gb",
    "mig-7g.186gb",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MIGProfileType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MIGProfileType:
    return cast(MIGProfileType, data)
