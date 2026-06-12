"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetDevice``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_sagemaker.errors import DeserializationError

TargetDevice: TypeAlias = Literal[
    "lambda",
    "ml_m4",
    "ml_m5",
    "ml_m6g",
    "ml_c4",
    "ml_c5",
    "ml_c6g",
    "ml_p2",
    "ml_p3",
    "ml_g4dn",
    "ml_inf1",
    "ml_inf2",
    "ml_trn1",
    "ml_eia2",
    "jetson_tx1",
    "jetson_tx2",
    "jetson_nano",
    "jetson_xavier",
    "rasp3b",
    "rasp4b",
    "imx8qm",
    "deeplens",
    "rk3399",
    "rk3288",
    "aisage",
    "sbe_c",
    "qcs605",
    "qcs603",
    "sitara_am57x",
    "amba_cv2",
    "amba_cv22",
    "amba_cv25",
    "x86_win32",
    "x86_win64",
    "coreml",
    "jacinto_tda4vm",
    "imx8mplus",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "lambda",
        "ml_m4",
        "ml_m5",
        "ml_m6g",
        "ml_c4",
        "ml_c5",
        "ml_c6g",
        "ml_p2",
        "ml_p3",
        "ml_g4dn",
        "ml_inf1",
        "ml_inf2",
        "ml_trn1",
        "ml_eia2",
        "jetson_tx1",
        "jetson_tx2",
        "jetson_nano",
        "jetson_xavier",
        "rasp3b",
        "rasp4b",
        "imx8qm",
        "deeplens",
        "rk3399",
        "rk3288",
        "aisage",
        "sbe_c",
        "qcs605",
        "qcs603",
        "sitara_am57x",
        "amba_cv2",
        "amba_cv22",
        "amba_cv25",
        "x86_win32",
        "x86_win64",
        "coreml",
        "jacinto_tda4vm",
        "imx8mplus",
    )
)


def serialize_aws_json_1_1(value: TargetDevice) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetDevice:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetDevice value: {data!r}")
    return cast(TargetDevice, data)
