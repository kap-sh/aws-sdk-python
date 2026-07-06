"""Generated from Smithy shape ``com.amazonaws.efs#FileSystemDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_efs.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_efs.types.availability_zone_id
    import aws_sdk_efs.types.availability_zone_name
    import aws_sdk_efs.types.aws_account_id
    import aws_sdk_efs.types.creation_token
    import aws_sdk_efs.types.encrypted
    import aws_sdk_efs.types.file_system_arn
    import aws_sdk_efs.types.file_system_id
    import aws_sdk_efs.types.file_system_protection_description
    import aws_sdk_efs.types.file_system_size
    import aws_sdk_efs.types.kms_key_id
    import aws_sdk_efs.types.life_cycle_state
    import aws_sdk_efs.types.mount_target_count
    import aws_sdk_efs.types.performance_mode
    import aws_sdk_efs.types.provisioned_throughput_in_mibps
    import aws_sdk_efs.types.tag_value
    import aws_sdk_efs.types.tags
    import aws_sdk_efs.types.throughput_mode
    import aws_sdk_efs.types.timestamp


class FileSystemDescription(TypedDict, closed=True):
    owner_id: "aws_sdk_efs.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account that created the file system.</p>"""
    creation_token: "aws_sdk_efs.types.creation_token.CreationToken"
    """<p>The opaque string specified in the request.</p>"""
    file_system_id: "aws_sdk_efs.types.file_system_id.FileSystemId"
    """<p>The ID of the file system, assigned by Amazon EFS.</p>"""
    file_system_arn: NotRequired["aws_sdk_efs.types.file_system_arn.FileSystemArn"]
    """<p>The Amazon Resource Name (ARN) for the EFS file system, in the format <code>arn:aws:elasticfilesystem:<i>region</i>:<i>account-id</i>:file-system/<i>file-system-id</i> </code>. Example with sample data: <code>arn:aws:elasticfilesystem:us-west-2:1111333322228888:file-system/fs-01234567</code> </p>"""
    creation_time: "aws_sdk_efs.types.timestamp.Timestamp"
    """<p>The time that the file system was created, in seconds (since 1970-01-01T00:00:00Z).</p>"""
    life_cycle_state: "aws_sdk_efs.types.life_cycle_state.LifeCycleState"
    """<p>The lifecycle phase of the file system.</p>"""
    name: NotRequired["aws_sdk_efs.types.tag_value.TagValue"]
    """<p>You can add tags to a file system, including a <code>Name</code> tag. For more information, see <a>CreateFileSystem</a>. If the file system has a <code>Name</code> tag, Amazon EFS returns the value in this field. </p>"""
    number_of_mount_targets: "aws_sdk_efs.types.mount_target_count.MountTargetCount"
    """<p>The current number of mount targets that the file system has. For more information, see <a>CreateMountTarget</a>.</p>"""
    size_in_bytes: "aws_sdk_efs.types.file_system_size.FileSystemSize"
    """<p>The latest known metered size (in bytes) of data stored in the file system, in its <code>Value</code> field, and the time at which that size was determined in its <code>Timestamp</code> field. The <code>Timestamp</code> value is the integer number of seconds since 1970-01-01T00:00:00Z. The <code>SizeInBytes</code> value doesn't represent the size of a consistent snapshot of the file system, but it is eventually consistent when there are no writes to the file system. That is, <code>SizeInBytes</code> represents actual size only if the file system is not modified for a period longer than a couple of hours. Otherwise, the value is not the exact size that the file system was at any point in time. </p>"""
    performance_mode: "aws_sdk_efs.types.performance_mode.PerformanceMode"
    """<p>The performance mode of the file system.</p>"""
    encrypted: NotRequired["aws_sdk_efs.types.encrypted.Encrypted"]
    """<p>A Boolean value that, if true, indicates that the file system is encrypted.</p>"""
    kms_key_id: NotRequired["aws_sdk_efs.types.kms_key_id.KmsKeyId"]
    """<p>The ID of an KMS key used to protect the encrypted file system.</p>"""
    throughput_mode: NotRequired["aws_sdk_efs.types.throughput_mode.ThroughputMode"]
    r"""<p>Displays the file system's throughput mode. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/performance.html#throughput-modes\">Throughput modes</a> in the <i>Amazon EFS User Guide</i>. </p>"""
    provisioned_throughput_in_mibps: NotRequired[
        "aws_sdk_efs.types.provisioned_throughput_in_mibps.ProvisionedThroughputInMibps"
    ]
    """<p>The amount of provisioned throughput, measured in MiBps, for the file system. Valid for file systems using <code>ThroughputMode</code> set to <code>provisioned</code>.</p>"""
    availability_zone_name: NotRequired[
        "aws_sdk_efs.types.availability_zone_name.AvailabilityZoneName"
    ]
    r"""<p>Describes the Amazon Web Services Availability Zone in which the file system is located, and is valid only for One Zone file systems. For more information, see <a href=\"https://docs.aws.amazon.com/efs/latest/ug/storage-classes.html\">Using EFS storage classes</a> in the <i>Amazon EFS User Guide</i>.</p>"""
    availability_zone_id: NotRequired[
        "aws_sdk_efs.types.availability_zone_id.AvailabilityZoneId"
    ]
    """<p>The unique and consistent identifier of the Availability Zone in which the file system is located, and is valid only for One Zone file systems. For example, <code>use1-az1</code> is an Availability Zone ID for the us-east-1 Amazon Web Services Region, and it has the same location in every Amazon Web Services account.</p>"""
    tags: "aws_sdk_efs.types.tags.Tags"
    """<p>The tags associated with the file system, presented as an array of <code>Tag</code> objects.</p>"""
    file_system_protection: NotRequired[
        "aws_sdk_efs.types.file_system_protection_description.FileSystemProtectionDescription"
    ]
    """<p>Describes the protection on the file system. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemDescription) -> dict:
    out: dict = {}
    out["OwnerId"] = value["owner_id"]
    out["CreationToken"] = value["creation_token"]
    out["FileSystemId"] = value["file_system_id"]
    if "file_system_arn" in value:
        out["FileSystemArn"] = value["file_system_arn"]
    import aws_sdk_efs.types.timestamp

    out["CreationTime"] = aws_sdk_efs.types.timestamp.serialize_json(
        value["creation_time"]
    )
    import aws_sdk_efs.types.life_cycle_state

    out["LifeCycleState"] = aws_sdk_efs.types.life_cycle_state.serialize_json(
        value["life_cycle_state"]
    )
    if "name" in value:
        out["Name"] = value["name"]
    out["NumberOfMountTargets"] = value.get("number_of_mount_targets", 0)
    import aws_sdk_efs.types.file_system_size

    out["SizeInBytes"] = aws_sdk_efs.types.file_system_size.serialize_json(
        value["size_in_bytes"]
    )
    import aws_sdk_efs.types.performance_mode

    out["PerformanceMode"] = aws_sdk_efs.types.performance_mode.serialize_json(
        value["performance_mode"]
    )
    if "encrypted" in value:
        out["Encrypted"] = value["encrypted"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "throughput_mode" in value:
        import aws_sdk_efs.types.throughput_mode

        out["ThroughputMode"] = aws_sdk_efs.types.throughput_mode.serialize_json(
            value["throughput_mode"]
        )
    if "provisioned_throughput_in_mibps" in value:
        out["ProvisionedThroughputInMibps"] = value["provisioned_throughput_in_mibps"]
    if "availability_zone_name" in value:
        out["AvailabilityZoneName"] = value["availability_zone_name"]
    if "availability_zone_id" in value:
        out["AvailabilityZoneId"] = value["availability_zone_id"]
    import aws_sdk_efs.types.tags

    out["Tags"] = aws_sdk_efs.types.tags.serialize_json(value["tags"])
    if "file_system_protection" in value:
        import aws_sdk_efs.types.file_system_protection_description

        out["FileSystemProtection"] = (
            aws_sdk_efs.types.file_system_protection_description.serialize_json(
                value["file_system_protection"]
            )
        )
    return out


def deserialize_json(data: dict) -> FileSystemDescription:
    out: FileSystemDescription = {}  # type: ignore[typeddict-item]
    if "OwnerId" in data:
        out["owner_id"] = data["OwnerId"]
    else:
        raise DeserializationError("FileSystemDescription.owner_id required")
    if "CreationToken" in data:
        out["creation_token"] = data["CreationToken"]
    else:
        raise DeserializationError("FileSystemDescription.creation_token required")
    if "FileSystemId" in data:
        out["file_system_id"] = data["FileSystemId"]
    else:
        raise DeserializationError("FileSystemDescription.file_system_id required")
    if "FileSystemArn" in data:
        out["file_system_arn"] = data["FileSystemArn"]
    if "CreationTime" in data:
        import aws_sdk_efs.types.timestamp

        out["creation_time"] = aws_sdk_efs.types.timestamp.deserialize_json(
            data["CreationTime"]
        )
    else:
        raise DeserializationError("FileSystemDescription.creation_time required")
    if "LifeCycleState" in data:
        import aws_sdk_efs.types.life_cycle_state

        out["life_cycle_state"] = aws_sdk_efs.types.life_cycle_state.deserialize_json(
            data["LifeCycleState"]
        )
    else:
        raise DeserializationError("FileSystemDescription.life_cycle_state required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "NumberOfMountTargets" in data:
        out["number_of_mount_targets"] = data["NumberOfMountTargets"]
    else:
        out["number_of_mount_targets"] = 0
    if "SizeInBytes" in data:
        import aws_sdk_efs.types.file_system_size

        out["size_in_bytes"] = aws_sdk_efs.types.file_system_size.deserialize_json(
            data["SizeInBytes"]
        )
    else:
        raise DeserializationError("FileSystemDescription.size_in_bytes required")
    if "PerformanceMode" in data:
        import aws_sdk_efs.types.performance_mode

        out["performance_mode"] = aws_sdk_efs.types.performance_mode.deserialize_json(
            data["PerformanceMode"]
        )
    else:
        raise DeserializationError("FileSystemDescription.performance_mode required")
    if "Encrypted" in data:
        out["encrypted"] = data["Encrypted"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "ThroughputMode" in data:
        import aws_sdk_efs.types.throughput_mode

        out["throughput_mode"] = aws_sdk_efs.types.throughput_mode.deserialize_json(
            data["ThroughputMode"]
        )
    if "ProvisionedThroughputInMibps" in data:
        out["provisioned_throughput_in_mibps"] = data["ProvisionedThroughputInMibps"]
    if "AvailabilityZoneName" in data:
        out["availability_zone_name"] = data["AvailabilityZoneName"]
    if "AvailabilityZoneId" in data:
        out["availability_zone_id"] = data["AvailabilityZoneId"]
    if "Tags" in data:
        import aws_sdk_efs.types.tags

        out["tags"] = aws_sdk_efs.types.tags.deserialize_json(data["Tags"])
    else:
        raise DeserializationError("FileSystemDescription.tags required")
    if "FileSystemProtection" in data:
        import aws_sdk_efs.types.file_system_protection_description

        out["file_system_protection"] = (
            aws_sdk_efs.types.file_system_protection_description.deserialize_json(
                data["FileSystemProtection"]
            )
        )
    return out
