"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateUploadRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_device_farm.types.amazon_resource_name
    import aws_sdk_device_farm.types.content_type
    import aws_sdk_device_farm.types.name
    import aws_sdk_device_farm.types.upload_type


class CreateUploadRequest(TypedDict):
    project_arn: "aws_sdk_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the project for the upload.</p>"""
    name: "aws_sdk_device_farm.types.name.Name"
    """<p>The upload's file name. The name should not contain any forward slashes (<code>/</code>). If you are uploading an iOS app, the file name must end with the <code>.ipa</code> extension. If you are uploading an Android app, the file name must end with the <code>.apk</code> extension. For all others, the file name must end with the <code>.zip</code> file extension.</p>"""
    type: "aws_sdk_device_farm.types.upload_type.UploadType"
    """<p>The upload's upload type.</p> <p>Must be one of the following values:</p> <ul> <li> <p>ANDROID_APP</p> </li> <li> <p>IOS_APP</p> </li> <li> <p>WEB_APP</p> </li> <li> <p>EXTERNAL_DATA</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_RUBY_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_PACKAGE</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_PACKAGE</p> </li> <li> <p>INSTRUMENTATION_TEST_PACKAGE</p> </li> <li> <p>XCTEST_TEST_PACKAGE</p> </li> <li> <p>XCTEST_UI_TEST_PACKAGE</p> </li> <li> <p>APPIUM_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_RUBY_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_JUNIT_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_JAVA_TESTNG_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_PYTHON_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_NODE_TEST_SPEC</p> </li> <li> <p>APPIUM_WEB_RUBY_TEST_SPEC</p> </li> <li> <p>INSTRUMENTATION_TEST_SPEC</p> </li> <li> <p>XCTEST_UI_TEST_SPEC</p> </li> </ul> <p> If you call <code>CreateUpload</code> with <code>WEB_APP</code> specified, AWS Device Farm throws an <code>ArgumentException</code> error.</p>"""
    content_type: NotRequired["aws_sdk_device_farm.types.content_type.ContentType"]
    """<p>The upload's content type (for example, <code>application/octet-stream</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUploadRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["name"] = value["name"]
    import aws_sdk_device_farm.types.upload_type

    out["type"] = aws_sdk_device_farm.types.upload_type.serialize_aws_json_1_1(
        value["type"]
    )
    if "content_type" in value:
        out["contentType"] = value["content_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUploadRequest:
    out: CreateUploadRequest = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("CreateUploadRequest.project_arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateUploadRequest.name required")
    if "type" in data:
        import aws_sdk_device_farm.types.upload_type

        out["type"] = aws_sdk_device_farm.types.upload_type.deserialize_aws_json_1_1(
            data["type"]
        )
    else:
        raise DeserializationError("CreateUploadRequest.type required")
    if "contentType" in data:
        out["content_type"] = data["contentType"]
    return out
