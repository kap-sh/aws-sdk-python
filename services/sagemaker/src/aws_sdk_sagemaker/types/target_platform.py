"""Generated from Smithy shape ``com.amazonaws.sagemaker#TargetPlatform``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.target_platform_accelerator
    import aws_sdk_sagemaker.types.target_platform_arch
    import aws_sdk_sagemaker.types.target_platform_os


class TargetPlatform(TypedDict):
    os: NotRequired["aws_sdk_sagemaker.types.target_platform_os.TargetPlatformOs"]
    r"""<p>Specifies a target platform OS.</p> <ul> <li> <p> <code>LINUX</code>: Linux-based operating systems.</p> </li> <li> <p> <code>ANDROID</code>: Android operating systems. Android API level can be specified using the <code>ANDROID_PLATFORM</code> compiler option. For example, <code>\"CompilerOptions\": {'ANDROID_PLATFORM': 28}</code> </p> </li> </ul>"""
    arch: NotRequired["aws_sdk_sagemaker.types.target_platform_arch.TargetPlatformArch"]
    """<p>Specifies a target platform architecture.</p> <ul> <li> <p> <code>X86_64</code>: 64-bit version of the x86 instruction set.</p> </li> <li> <p> <code>X86</code>: 32-bit version of the x86 instruction set.</p> </li> <li> <p> <code>ARM64</code>: ARMv8 64-bit CPU.</p> </li> <li> <p> <code>ARM_EABIHF</code>: ARMv7 32-bit, Hard Float.</p> </li> <li> <p> <code>ARM_EABI</code>: ARMv7 32-bit, Soft Float. Used by Android 32-bit ARM platform.</p> </li> </ul>"""
    accelerator: NotRequired[
        "aws_sdk_sagemaker.types.target_platform_accelerator.TargetPlatformAccelerator"
    ]
    """<p>Specifies a target platform accelerator (optional).</p> <ul> <li> <p> <code>NVIDIA</code>: Nvidia graphics processing unit. It also requires <code>gpu-code</code>, <code>trt-ver</code>, <code>cuda-ver</code> compiler options</p> </li> <li> <p> <code>MALI</code>: ARM Mali graphics processor</p> </li> <li> <p> <code>INTEL_GRAPHICS</code>: Integrated Intel graphics</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetPlatform) -> dict:
    out: dict = {}
    if "os" in value:
        import aws_sdk_sagemaker.types.target_platform_os

        out["Os"] = aws_sdk_sagemaker.types.target_platform_os.serialize_aws_json_1_1(
            value["os"]
        )
    if "arch" in value:
        import aws_sdk_sagemaker.types.target_platform_arch

        out["Arch"] = (
            aws_sdk_sagemaker.types.target_platform_arch.serialize_aws_json_1_1(
                value["arch"]
            )
        )
    if "accelerator" in value:
        import aws_sdk_sagemaker.types.target_platform_accelerator

        out["Accelerator"] = (
            aws_sdk_sagemaker.types.target_platform_accelerator.serialize_aws_json_1_1(
                value["accelerator"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetPlatform:
    out: TargetPlatform = {}  # type: ignore[typeddict-item]
    if "Os" in data:
        import aws_sdk_sagemaker.types.target_platform_os

        out["os"] = aws_sdk_sagemaker.types.target_platform_os.deserialize_aws_json_1_1(
            data["Os"]
        )
    if "Arch" in data:
        import aws_sdk_sagemaker.types.target_platform_arch

        out["arch"] = (
            aws_sdk_sagemaker.types.target_platform_arch.deserialize_aws_json_1_1(
                data["Arch"]
            )
        )
    if "Accelerator" in data:
        import aws_sdk_sagemaker.types.target_platform_accelerator

        out["accelerator"] = (
            aws_sdk_sagemaker.types.target_platform_accelerator.deserialize_aws_json_1_1(
                data["Accelerator"]
            )
        )
    return out
