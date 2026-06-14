from typing import TYPE_CHECKING, Optional

from aws_sdk_transfer._services._pipeline import (
    AsyncOperationRequest,
    AsyncOperationResponse,
    OperationRequest,
    OperationResponse,
    aexecute_pipeline,
    execute_pipeline,
)

if TYPE_CHECKING:
    import aws_sdk_transfer.types.certificate
    import aws_sdk_transfer.types.create_server_request
    import aws_sdk_transfer.types.create_server_response
    import aws_sdk_transfer.types.delete_server_request
    import aws_sdk_transfer.types.describe_server_request
    import aws_sdk_transfer.types.describe_server_response
    import aws_sdk_transfer.types.domain
    import aws_sdk_transfer.types.endpoint_details
    import aws_sdk_transfer.types.endpoint_type
    import aws_sdk_transfer.types.host_key
    import aws_sdk_transfer.types.identity_provider_details
    import aws_sdk_transfer.types.identity_provider_type
    import aws_sdk_transfer.types.ip_address_type
    import aws_sdk_transfer.types.list_servers_request
    import aws_sdk_transfer.types.list_servers_response
    import aws_sdk_transfer.types.listed_server
    import aws_sdk_transfer.types.max_results
    import aws_sdk_transfer.types.next_token
    import aws_sdk_transfer.types.nullable_role
    import aws_sdk_transfer.types.post_authentication_login_banner
    import aws_sdk_transfer.types.pre_authentication_login_banner
    import aws_sdk_transfer.types.protocol_details
    import aws_sdk_transfer.types.protocols
    import aws_sdk_transfer.types.s3_storage_options
    import aws_sdk_transfer.types.security_policy_name
    import aws_sdk_transfer.types.server_id
    import aws_sdk_transfer.types.structured_log_destinations
    import aws_sdk_transfer.types.tags
    import aws_sdk_transfer.types.update_server_request
    import aws_sdk_transfer.types.update_server_response
    import aws_sdk_transfer.types.workflow_details
    from aws_sdk_transfer._services.async_transfer import (
        AsyncTransferClient,
        AsyncTransferClientConfig,
    )
    from aws_sdk_transfer._services.transfer import TransferClient, TransferClientConfig


class ServerResource:
    def __init__(self, service: TransferClient) -> None:
        self._service = service

    def create(
        self,
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        certificate: Optional["aws_sdk_transfer.types.certificate.Certificate"] = None,
        domain: Optional["aws_sdk_transfer.types.domain.Domain"] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.endpoint_details.EndpointDetails"
        ] = None,
        endpoint_type: Optional[
            "aws_sdk_transfer.types.endpoint_type.EndpointType"
        ] = None,
        host_key: Optional["aws_sdk_transfer.types.host_key.HostKey"] = None,
        identity_provider_details: Optional[
            "aws_sdk_transfer.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        identity_provider_type: Optional[
            "aws_sdk_transfer.types.identity_provider_type.IdentityProviderType"
        ] = None,
        logging_role: Optional[
            "aws_sdk_transfer.types.nullable_role.NullableRole"
        ] = None,
        post_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
        ] = None,
        pre_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
        ] = None,
        protocols: Optional["aws_sdk_transfer.types.protocols.Protocols"] = None,
        protocol_details: Optional[
            "aws_sdk_transfer.types.protocol_details.ProtocolDetails"
        ] = None,
        security_policy_name: Optional[
            "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
        workflow_details: Optional[
            "aws_sdk_transfer.types.workflow_details.WorkflowDetails"
        ] = None,
        structured_log_destinations: Optional[
            "aws_sdk_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
        s3_storage_options: Optional[
            "aws_sdk_transfer.types.s3_storage_options.S3StorageOptions"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_transfer.types.ip_address_type.IpAddressType"
        ] = None,
    ) -> "aws_sdk_transfer.types.create_server_response.CreateServerResponse":
        r"""<p>Instantiates an auto-scaling virtual server based on the selected file transfer protocol in Amazon Web Services. When you make updates to your file transfer protocol-enabled server or when you work with users, use the service-generated <code>ServerId</code> property that is assigned to the newly created server.</p>

        Args:
            certificate: <p>The Amazon Resource Name (ARN) of the Certificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p> <p>To request a new public certificate, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html\">Request a public certificate</a> in the <i>Certificate Manager User Guide</i>.</p> <p>To import an existing certificate into ACM, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing certificates into ACM</a> in the <i>Certificate Manager User Guide</i>.</p> <p>To request a private certificate to use FTPS through private IP addresses, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html\">Request a private certificate</a> in the <i>Certificate Manager User Guide</i>.</p> <p>Certificates with the following cryptographic algorithms and key sizes are supported:</p> <ul> <li> <p>2048-bit RSA (RSA_2048)</p> </li> <li> <p>4096-bit RSA (RSA_4096)</p> </li> <li> <p>Elliptic Prime Curve 256 bit (EC_prime256v1)</p> </li> <li> <p>Elliptic Prime Curve 384 bit (EC_secp384r1)</p> </li> <li> <p>Elliptic Prime Curve 521 bit (EC_secp521r1)</p> </li> </ul> <note> <p>The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.</p> </note>
            domain: <p>The domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.</p> <note> <p>After the server is created, the domain cannot be changed.</p> </note>
            endpoint_details: <p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>
            endpoint_type: <p>The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> <p>It is recommended that you use <code>VPC</code> as the <code>EndpointType</code>. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with <code>EndpointType</code> set to <code>VPC_ENDPOINT</code>.</p> </note>
            host_key: <p>The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.</p> <p>Use the following command to generate an RSA 2048 bit key with no passphrase:</p> <p> <code>ssh-keygen -t rsa -b 2048 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Use a minimum value of 2048 for the <code>-b</code> option. You can create a stronger key by using 3072 or 4096.</p> <p>Use the following command to generate an ECDSA 256 bit key with no passphrase:</p> <p> <code>ssh-keygen -t ecdsa -b 256 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Valid values for the <code>-b</code> option for ECDSA are 256, 384, and 521.</p> <p>Use the following command to generate an ED25519 key with no passphrase:</p> <p> <code>ssh-keygen -t ed25519 -N \"\" -f my-new-server-key</code>.</p> <p>For all of these commands, you can replace <i>my-new-server-key</i> with a string of your choice.</p> <important> <p>If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.</p> </important> <p>For more information, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key\">Manage host keys for your SFTP-enabled server</a> in the <i>Transfer Family User Guide</i>.</p>
            identity_provider_details: <p>Required when <code>IdentityProviderType</code> is set to <code>AWS_DIRECTORY_SERVICE</code>, <code>Amazon Web Services_LAMBDA</code> or <code>API_GATEWAY</code>. Accepts an array containing all of the information required to use a directory in <code>AWS_DIRECTORY_SERVICE</code> or invoke a customer-supplied authentication API, including the API Gateway URL. Cannot be specified when <code>IdentityProviderType</code> is set to <code>SERVICE_MANAGED</code>.</p>
            identity_provider_type: <p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>
            post_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>
            pre_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>
            protocols: <p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>
            protocol_details: <p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations\"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>
            security_policy_name: <p>Specifies the name of the security policy for the server.</p>
            tags: <p>Key-value pairs that can be used to group and search for servers.</p>
            workflow_details: <p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p>
            structured_log_destinations: <p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>
            s3_storage_options: <p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>
            ip_address_type: <p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href=\"https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html\">EndpointDetails</a> for the server.</p> </note>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.create_server_request.CreateServerRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.create_server_response.CreateServerResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_server

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.create_server.create_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.create_server_request.CreateServerRequest = {}  # type: ignore[typeddict-item]
        if certificate is not None:
            input_["certificate"] = certificate
        if domain is not None:
            input_["domain"] = domain
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if host_key is not None:
            input_["host_key"] = host_key
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            input_["post_authentication_login_banner"] = (
                post_authentication_login_banner
            )
        if pre_authentication_login_banner is not None:
            input_["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocols is not None:
            input_["protocols"] = protocols
        if protocol_details is not None:
            input_["protocol_details"] = protocol_details
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if tags is not None:
            input_["tags"] = tags
        if workflow_details is not None:
            input_["workflow_details"] = workflow_details
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations
        if s3_storage_options is not None:
            input_["s3_storage_options"] = s3_storage_options
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def read(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_server_response.DescribeServerResponse":
        """<p>Describes a file transfer protocol-enabled server that you specify by passing the <code>ServerId</code> parameter.</p> <p>The response contains a description of a server's properties. When you set <code>EndpointType</code> to VPC, the response will contain the <code>EndpointDetails</code>.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.describe_server_request.DescribeServerRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.describe_server_response.DescribeServerResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_server

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.describe_server.describe_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_server_request.DescribeServerRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def update(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        certificate: Optional["aws_sdk_transfer.types.certificate.Certificate"] = None,
        protocol_details: Optional[
            "aws_sdk_transfer.types.protocol_details.ProtocolDetails"
        ] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.endpoint_details.EndpointDetails"
        ] = None,
        endpoint_type: Optional[
            "aws_sdk_transfer.types.endpoint_type.EndpointType"
        ] = None,
        host_key: Optional["aws_sdk_transfer.types.host_key.HostKey"] = None,
        identity_provider_details: Optional[
            "aws_sdk_transfer.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        logging_role: Optional[
            "aws_sdk_transfer.types.nullable_role.NullableRole"
        ] = None,
        post_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
        ] = None,
        pre_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
        ] = None,
        protocols: Optional["aws_sdk_transfer.types.protocols.Protocols"] = None,
        security_policy_name: Optional[
            "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName"
        ] = None,
        workflow_details: Optional[
            "aws_sdk_transfer.types.workflow_details.WorkflowDetails"
        ] = None,
        structured_log_destinations: Optional[
            "aws_sdk_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
        s3_storage_options: Optional[
            "aws_sdk_transfer.types.s3_storage_options.S3StorageOptions"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_transfer.types.ip_address_type.IpAddressType"
        ] = None,
        identity_provider_type: Optional[
            "aws_sdk_transfer.types.identity_provider_type.IdentityProviderType"
        ] = None,
    ) -> "aws_sdk_transfer.types.update_server_response.UpdateServerResponse":
        r"""<p>Updates the file transfer protocol-enabled server's properties after that server has been created.</p> <p>The <code>UpdateServer</code> call returns the <code>ServerId</code> of the server you updated.</p>

        Args:
            certificate: <p>The Amazon Resource Name (ARN) of the Amazon Web ServicesCertificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p> <p>To request a new public certificate, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html\">Request a public certificate</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>To import an existing certificate into ACM, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing certificates into ACM</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>To request a private certificate to use FTPS through private IP addresses, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html\">Request a private certificate</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>Certificates with the following cryptographic algorithms and key sizes are supported:</p> <ul> <li> <p>2048-bit RSA (RSA_2048)</p> </li> <li> <p>4096-bit RSA (RSA_4096)</p> </li> <li> <p>Elliptic Prime Curve 256 bit (EC_prime256v1)</p> </li> <li> <p>Elliptic Prime Curve 384 bit (EC_secp384r1)</p> </li> <li> <p>Elliptic Prime Curve 521 bit (EC_secp521r1)</p> </li> </ul> <note> <p>The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.</p> </note>
            protocol_details: <p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations\"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>
            endpoint_details: <p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>
            endpoint_type: <p>The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> <p>It is recommended that you use <code>VPC</code> as the <code>EndpointType</code>. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with <code>EndpointType</code> set to <code>VPC_ENDPOINT</code>.</p> </note>
            host_key: <p>The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.</p> <p>Use the following command to generate an RSA 2048 bit key with no passphrase:</p> <p> <code>ssh-keygen -t rsa -b 2048 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Use a minimum value of 2048 for the <code>-b</code> option. You can create a stronger key by using 3072 or 4096.</p> <p>Use the following command to generate an ECDSA 256 bit key with no passphrase:</p> <p> <code>ssh-keygen -t ecdsa -b 256 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Valid values for the <code>-b</code> option for ECDSA are 256, 384, and 521.</p> <p>Use the following command to generate an ED25519 key with no passphrase:</p> <p> <code>ssh-keygen -t ed25519 -N \"\" -f my-new-server-key</code>.</p> <p>For all of these commands, you can replace <i>my-new-server-key</i> with a string of your choice.</p> <important> <p>If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.</p> </important> <p>For more information, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key\">Manage host keys for your SFTP-enabled server</a> in the <i>Transfer Family User Guide</i>.</p>
            identity_provider_details: <p>An array containing all of the information required to call a customer's authentication API method.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>
            post_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>
            pre_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>
            protocols: <p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>
            security_policy_name: <p>Specifies the name of the security policy for the server.</p>
            server_id: <p>A system-assigned unique identifier for a server instance that the Transfer Family user is assigned to.</p>
            workflow_details: <p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p> <p>To remove an associated workflow from a server, you can provide an empty <code>OnUpload</code> object, as in the following example.</p> <p> <code>aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{\"OnUpload\":[]}'</code> </p>
            structured_log_destinations: <p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>
            s3_storage_options: <p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>
            ip_address_type: <p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href=\"https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html\">EndpointDetails</a> for the server.</p> </note>
            identity_provider_type: <p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.update_server_request.UpdateServerRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.update_server_response.UpdateServerResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_server

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.update_server.update_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.update_server_request.UpdateServerRequest = {}  # type: ignore[typeddict-item]
        if certificate is not None:
            input_["certificate"] = certificate
        if protocol_details is not None:
            input_["protocol_details"] = protocol_details
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if host_key is not None:
            input_["host_key"] = host_key
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            input_["post_authentication_login_banner"] = (
                post_authentication_login_banner
            )
        if pre_authentication_login_banner is not None:
            input_["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocols is not None:
            input_["protocols"] = protocols
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        input_["server_id"] = server_id
        if workflow_details is not None:
            input_["workflow_details"] = workflow_details
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations
        if s3_storage_options is not None:
            input_["s3_storage_options"] = s3_storage_options
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def delete(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[TransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the file transfer protocol-enabled server that you specify.</p> <p>No response returns from this operation.</p>

        Args:
            server_id: <p>A unique system-assigned identifier for a server instance.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.delete_server_request.DeleteServerRequest]",
        ) -> OperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_server

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.delete_server.delete_server(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_server_request.DeleteServerRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    def list(
        self,
        *,
        config_overrides: Optional[TransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_servers_response.ListServersResponse":
        """<p>Lists the file transfer protocol-enabled servers that are associated with your Amazon Web Services account.</p>

        Args:
            max_results: <p>Specifies the number of servers to return as a response to the <code>ListServers</code> query.</p>
            next_token: <p>When additional results are obtained from the <code>ListServers</code> command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional servers.</p>
        """

        def _handler(
            req: "OperationRequest[aws_sdk_transfer.types.list_servers_request.ListServersRequest]",
        ) -> OperationResponse[
            "aws_sdk_transfer.types.list_servers_response.ListServersResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_servers

            output, http_response = (
                aws_sdk_transfer._operations.transfer_service.list_servers.list_servers(
                    req.options, req.input
                )
            )
            return OperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_servers_request.ListServersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = execute_pipeline(
            OperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output


class AsyncServerResource:
    def __init__(self, service: AsyncTransferClient) -> None:
        self._service = service

    async def create(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate: Optional["aws_sdk_transfer.types.certificate.Certificate"] = None,
        domain: Optional["aws_sdk_transfer.types.domain.Domain"] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.endpoint_details.EndpointDetails"
        ] = None,
        endpoint_type: Optional[
            "aws_sdk_transfer.types.endpoint_type.EndpointType"
        ] = None,
        host_key: Optional["aws_sdk_transfer.types.host_key.HostKey"] = None,
        identity_provider_details: Optional[
            "aws_sdk_transfer.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        identity_provider_type: Optional[
            "aws_sdk_transfer.types.identity_provider_type.IdentityProviderType"
        ] = None,
        logging_role: Optional[
            "aws_sdk_transfer.types.nullable_role.NullableRole"
        ] = None,
        post_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
        ] = None,
        pre_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
        ] = None,
        protocols: Optional["aws_sdk_transfer.types.protocols.Protocols"] = None,
        protocol_details: Optional[
            "aws_sdk_transfer.types.protocol_details.ProtocolDetails"
        ] = None,
        security_policy_name: Optional[
            "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName"
        ] = None,
        tags: Optional["aws_sdk_transfer.types.tags.Tags"] = None,
        workflow_details: Optional[
            "aws_sdk_transfer.types.workflow_details.WorkflowDetails"
        ] = None,
        structured_log_destinations: Optional[
            "aws_sdk_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
        s3_storage_options: Optional[
            "aws_sdk_transfer.types.s3_storage_options.S3StorageOptions"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_transfer.types.ip_address_type.IpAddressType"
        ] = None,
    ) -> "aws_sdk_transfer.types.create_server_response.CreateServerResponse":
        r"""<p>Instantiates an auto-scaling virtual server based on the selected file transfer protocol in Amazon Web Services. When you make updates to your file transfer protocol-enabled server or when you work with users, use the service-generated <code>ServerId</code> property that is assigned to the newly created server.</p>

        Args:
            certificate: <p>The Amazon Resource Name (ARN) of the Certificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p> <p>To request a new public certificate, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html\">Request a public certificate</a> in the <i>Certificate Manager User Guide</i>.</p> <p>To import an existing certificate into ACM, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing certificates into ACM</a> in the <i>Certificate Manager User Guide</i>.</p> <p>To request a private certificate to use FTPS through private IP addresses, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html\">Request a private certificate</a> in the <i>Certificate Manager User Guide</i>.</p> <p>Certificates with the following cryptographic algorithms and key sizes are supported:</p> <ul> <li> <p>2048-bit RSA (RSA_2048)</p> </li> <li> <p>4096-bit RSA (RSA_4096)</p> </li> <li> <p>Elliptic Prime Curve 256 bit (EC_prime256v1)</p> </li> <li> <p>Elliptic Prime Curve 384 bit (EC_secp384r1)</p> </li> <li> <p>Elliptic Prime Curve 521 bit (EC_secp521r1)</p> </li> </ul> <note> <p>The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.</p> </note>
            domain: <p>The domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.</p> <note> <p>After the server is created, the domain cannot be changed.</p> </note>
            endpoint_details: <p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>
            endpoint_type: <p>The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> <p>It is recommended that you use <code>VPC</code> as the <code>EndpointType</code>. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with <code>EndpointType</code> set to <code>VPC_ENDPOINT</code>.</p> </note>
            host_key: <p>The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.</p> <p>Use the following command to generate an RSA 2048 bit key with no passphrase:</p> <p> <code>ssh-keygen -t rsa -b 2048 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Use a minimum value of 2048 for the <code>-b</code> option. You can create a stronger key by using 3072 or 4096.</p> <p>Use the following command to generate an ECDSA 256 bit key with no passphrase:</p> <p> <code>ssh-keygen -t ecdsa -b 256 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Valid values for the <code>-b</code> option for ECDSA are 256, 384, and 521.</p> <p>Use the following command to generate an ED25519 key with no passphrase:</p> <p> <code>ssh-keygen -t ed25519 -N \"\" -f my-new-server-key</code>.</p> <p>For all of these commands, you can replace <i>my-new-server-key</i> with a string of your choice.</p> <important> <p>If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.</p> </important> <p>For more information, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key\">Manage host keys for your SFTP-enabled server</a> in the <i>Transfer Family User Guide</i>.</p>
            identity_provider_details: <p>Required when <code>IdentityProviderType</code> is set to <code>AWS_DIRECTORY_SERVICE</code>, <code>Amazon Web Services_LAMBDA</code> or <code>API_GATEWAY</code>. Accepts an array containing all of the information required to use a directory in <code>AWS_DIRECTORY_SERVICE</code> or invoke a customer-supplied authentication API, including the API Gateway URL. Cannot be specified when <code>IdentityProviderType</code> is set to <code>SERVICE_MANAGED</code>.</p>
            identity_provider_type: <p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>
            post_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>
            pre_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>
            protocols: <p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>
            protocol_details: <p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations\"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>
            security_policy_name: <p>Specifies the name of the security policy for the server.</p>
            tags: <p>Key-value pairs that can be used to group and search for servers.</p>
            workflow_details: <p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p>
            structured_log_destinations: <p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>
            s3_storage_options: <p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>
            ip_address_type: <p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href=\"https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html\">EndpointDetails</a> for the server.</p> </note>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.create_server_request.CreateServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.create_server_response.CreateServerResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.create_server

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.create_server.async_create_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.create_server_request.CreateServerRequest = {}  # type: ignore[typeddict-item]
        if certificate is not None:
            input_["certificate"] = certificate
        if domain is not None:
            input_["domain"] = domain
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if host_key is not None:
            input_["host_key"] = host_key
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            input_["post_authentication_login_banner"] = (
                post_authentication_login_banner
            )
        if pre_authentication_login_banner is not None:
            input_["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocols is not None:
            input_["protocols"] = protocols
        if protocol_details is not None:
            input_["protocol_details"] = protocol_details
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        if tags is not None:
            input_["tags"] = tags
        if workflow_details is not None:
            input_["workflow_details"] = workflow_details
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations
        if s3_storage_options is not None:
            input_["s3_storage_options"] = s3_storage_options
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def read(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> "aws_sdk_transfer.types.describe_server_response.DescribeServerResponse":
        """<p>Describes a file transfer protocol-enabled server that you specify by passing the <code>ServerId</code> parameter.</p> <p>The response contains a description of a server's properties. When you set <code>EndpointType</code> to VPC, the response will contain the <code>EndpointDetails</code>.</p>

        Args:
            server_id: <p>A system-assigned unique identifier for a server.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.describe_server_request.DescribeServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.describe_server_response.DescribeServerResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.describe_server

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.describe_server.async_describe_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.describe_server_request.DescribeServerRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def update(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        certificate: Optional["aws_sdk_transfer.types.certificate.Certificate"] = None,
        protocol_details: Optional[
            "aws_sdk_transfer.types.protocol_details.ProtocolDetails"
        ] = None,
        endpoint_details: Optional[
            "aws_sdk_transfer.types.endpoint_details.EndpointDetails"
        ] = None,
        endpoint_type: Optional[
            "aws_sdk_transfer.types.endpoint_type.EndpointType"
        ] = None,
        host_key: Optional["aws_sdk_transfer.types.host_key.HostKey"] = None,
        identity_provider_details: Optional[
            "aws_sdk_transfer.types.identity_provider_details.IdentityProviderDetails"
        ] = None,
        logging_role: Optional[
            "aws_sdk_transfer.types.nullable_role.NullableRole"
        ] = None,
        post_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.post_authentication_login_banner.PostAuthenticationLoginBanner"
        ] = None,
        pre_authentication_login_banner: Optional[
            "aws_sdk_transfer.types.pre_authentication_login_banner.PreAuthenticationLoginBanner"
        ] = None,
        protocols: Optional["aws_sdk_transfer.types.protocols.Protocols"] = None,
        security_policy_name: Optional[
            "aws_sdk_transfer.types.security_policy_name.SecurityPolicyName"
        ] = None,
        workflow_details: Optional[
            "aws_sdk_transfer.types.workflow_details.WorkflowDetails"
        ] = None,
        structured_log_destinations: Optional[
            "aws_sdk_transfer.types.structured_log_destinations.StructuredLogDestinations"
        ] = None,
        s3_storage_options: Optional[
            "aws_sdk_transfer.types.s3_storage_options.S3StorageOptions"
        ] = None,
        ip_address_type: Optional[
            "aws_sdk_transfer.types.ip_address_type.IpAddressType"
        ] = None,
        identity_provider_type: Optional[
            "aws_sdk_transfer.types.identity_provider_type.IdentityProviderType"
        ] = None,
    ) -> "aws_sdk_transfer.types.update_server_response.UpdateServerResponse":
        r"""<p>Updates the file transfer protocol-enabled server's properties after that server has been created.</p> <p>The <code>UpdateServer</code> call returns the <code>ServerId</code> of the server you updated.</p>

        Args:
            certificate: <p>The Amazon Resource Name (ARN) of the Amazon Web ServicesCertificate Manager (ACM) certificate. Required when <code>Protocols</code> is set to <code>FTPS</code>.</p> <p>To request a new public certificate, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html\">Request a public certificate</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>To import an existing certificate into ACM, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html\">Importing certificates into ACM</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>To request a private certificate to use FTPS through private IP addresses, see <a href=\"https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html\">Request a private certificate</a> in the <i> Amazon Web ServicesCertificate Manager User Guide</i>.</p> <p>Certificates with the following cryptographic algorithms and key sizes are supported:</p> <ul> <li> <p>2048-bit RSA (RSA_2048)</p> </li> <li> <p>4096-bit RSA (RSA_4096)</p> </li> <li> <p>Elliptic Prime Curve 256 bit (EC_prime256v1)</p> </li> <li> <p>Elliptic Prime Curve 384 bit (EC_secp384r1)</p> </li> <li> <p>Elliptic Prime Curve 521 bit (EC_secp521r1)</p> </li> </ul> <note> <p>The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.</p> </note>
            protocol_details: <p>The protocol settings that are configured for your server.</p> <note> <p>Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations\"> Avoid placing NLBs and NATs in front of Transfer Family</a>.</p> </note> <ul> <li> <p> To indicate passive mode (for FTP and FTPS protocols), use the <code>PassiveIp</code> parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. </p> </li> <li> <p>To ignore the error that is generated when the client attempts to use the <code>SETSTAT</code> command on a file that you are uploading to an Amazon S3 bucket, use the <code>SetStatOption</code> parameter. To have the Transfer Family server ignore the <code>SETSTAT</code> command and upload files without needing to make any changes to your SFTP client, set the value to <code>ENABLE_NO_OP</code>. If you set the <code>SetStatOption</code> parameter to <code>ENABLE_NO_OP</code>, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a <code>SETSTAT</code> call.</p> </li> <li> <p>To determine whether your Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the <code>TlsSessionResumptionMode</code> parameter.</p> </li> <li> <p> <code>As2Transports</code> indicates the transport method for the AS2 messages. Currently, only HTTP is supported.</p> </li> </ul>
            endpoint_details: <p>The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.</p>
            endpoint_type: <p>The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.</p> <note> <p> After May 19, 2021, you won't be able to create a server using <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account if your account hasn't already done so before May 19, 2021. If you have already created servers with <code>EndpointType=VPC_ENDPOINT</code> in your Amazon Web Services account on or before May 19, 2021, you will not be affected. After this date, use <code>EndpointType</code>=<code>VPC</code>.</p> <p>For more information, see https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint.</p> <p>It is recommended that you use <code>VPC</code> as the <code>EndpointType</code>. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with <code>EndpointType</code> set to <code>VPC_ENDPOINT</code>.</p> </note>
            host_key: <p>The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.</p> <p>Use the following command to generate an RSA 2048 bit key with no passphrase:</p> <p> <code>ssh-keygen -t rsa -b 2048 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Use a minimum value of 2048 for the <code>-b</code> option. You can create a stronger key by using 3072 or 4096.</p> <p>Use the following command to generate an ECDSA 256 bit key with no passphrase:</p> <p> <code>ssh-keygen -t ecdsa -b 256 -N \"\" -m PEM -f my-new-server-key</code>.</p> <p>Valid values for the <code>-b</code> option for ECDSA are 256, 384, and 521.</p> <p>Use the following command to generate an ED25519 key with no passphrase:</p> <p> <code>ssh-keygen -t ed25519 -N \"\" -f my-new-server-key</code>.</p> <p>For all of these commands, you can replace <i>my-new-server-key</i> with a string of your choice.</p> <important> <p>If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.</p> </important> <p>For more information, see <a href=\"https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key\">Manage host keys for your SFTP-enabled server</a> in the <i>Transfer Family User Guide</i>.</p>
            identity_provider_details: <p>An array containing all of the information required to call a customer's authentication API method.</p>
            logging_role: <p>The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.</p>
            post_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.</p> <note> <p>The SFTP protocol does not support post-authentication display banners.</p> </note>
            pre_authentication_login_banner: <p>Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:</p> <p> <code>This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.</code> </p>
            protocols: <p>Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:</p> <ul> <li> <p> <code>SFTP</code> (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH</p> </li> <li> <p> <code>FTPS</code> (File Transfer Protocol Secure): File transfer with TLS encryption</p> </li> <li> <p> <code>FTP</code> (File Transfer Protocol): Unencrypted file transfer</p> </li> <li> <p> <code>AS2</code> (Applicability Statement 2): used for transporting structured business-to-business data</p> </li> </ul> <note> <ul> <li> <p>If you select <code>FTPS</code>, you must choose a certificate stored in Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.</p> </li> <li> <p>If <code>Protocol</code> includes either <code>FTP</code> or <code>FTPS</code>, then the <code>EndpointType</code> must be <code>VPC</code> and the <code>IdentityProviderType</code> must be either <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>FTP</code>, then <code>AddressAllocationIds</code> cannot be associated.</p> </li> <li> <p>If <code>Protocol</code> is set only to <code>SFTP</code>, the <code>EndpointType</code> can be set to <code>PUBLIC</code> and the <code>IdentityProviderType</code> can be set any of the supported identity types: <code>SERVICE_MANAGED</code>, <code>AWS_DIRECTORY_SERVICE</code>, <code>AWS_LAMBDA</code>, or <code>API_GATEWAY</code>.</p> </li> <li> <p>If <code>Protocol</code> includes <code>AS2</code>, then the <code>EndpointType</code> must be <code>VPC</code>, and domain must be Amazon S3.</p> </li> </ul> </note>
            security_policy_name: <p>Specifies the name of the security policy for the server.</p>
            server_id: <p>A system-assigned unique identifier for a server instance that the Transfer Family user is assigned to.</p>
            workflow_details: <p>Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.</p> <p>In addition to a workflow to execute when a file is uploaded completely, <code>WorkflowDetails</code> can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.</p> <p>To remove an associated workflow from a server, you can provide an empty <code>OnUpload</code> object, as in the following example.</p> <p> <code>aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{\"OnUpload\":[]}'</code> </p>
            structured_log_destinations: <p>Specifies the log groups to which your server logs are sent.</p> <p>To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:</p> <p> <code>arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*</code> </p> <p>For example, <code>arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*</code> </p> <p>If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an <code>update-server</code> call. For example:</p> <p> <code>update-server --server-id s-1234567890abcdef0 --structured-log-destinations</code> </p>
            s3_storage_options: <p>Specifies whether or not performance for your Amazon S3 directories is optimized.</p> <ul> <li> <p>If using the console, this is enabled by default.</p> </li> <li> <p>If using the API or CLI, this is disabled by default.</p> </li> </ul> <p>By default, home directory mappings have a <code>TYPE</code> of <code>DIRECTORY</code>. If you enable this option, you would then need to explicitly set the <code>HomeDirectoryMapEntry</code> <code>Type</code> to <code>FILE</code> if you want a mapping to have a file target.</p>
            ip_address_type: <p>Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your Transfer Family endpoint. The default value is <code>IPV4</code>.</p> <important> <p>The <code>IpAddressType</code> parameter has the following limitations:</p> <ul> <li> <p>It cannot be changed while the server is online. You must stop the server before modifying this parameter.</p> </li> <li> <p>It cannot be updated to <code>DUALSTACK</code> if the server has <code>AddressAllocationIds</code> specified.</p> </li> </ul> </important> <note> <p>When using <code>DUALSTACK</code> as the <code>IpAddressType</code>, you cannot set the <code>AddressAllocationIds</code> parameter for the <a href=\"https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html\">EndpointDetails</a> for the server.</p> </note>
            identity_provider_type: <p>The mode of authentication for a server. The default value is <code>SERVICE_MANAGED</code>, which allows you to store and access user credentials within the Transfer Family service.</p> <p>Use <code>AWS_DIRECTORY_SERVICE</code> to provide access to Active Directory groups in Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in Amazon Web Services using AD Connector. This option also requires you to provide a Directory ID by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>API_GATEWAY</code> value to integrate with an identity provider of your choosing. The <code>API_GATEWAY</code> setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the <code>IdentityProviderDetails</code> parameter.</p> <p>Use the <code>AWS_LAMBDA</code> value to directly use an Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the <code>Function</code> parameter for the <code>IdentityProviderDetails</code> data type.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.update_server_request.UpdateServerRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.update_server_response.UpdateServerResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.update_server

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.update_server.async_update_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.update_server_request.UpdateServerRequest = {}  # type: ignore[typeddict-item]
        if certificate is not None:
            input_["certificate"] = certificate
        if protocol_details is not None:
            input_["protocol_details"] = protocol_details
        if endpoint_details is not None:
            input_["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            input_["endpoint_type"] = endpoint_type
        if host_key is not None:
            input_["host_key"] = host_key
        if identity_provider_details is not None:
            input_["identity_provider_details"] = identity_provider_details
        if logging_role is not None:
            input_["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            input_["post_authentication_login_banner"] = (
                post_authentication_login_banner
            )
        if pre_authentication_login_banner is not None:
            input_["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocols is not None:
            input_["protocols"] = protocols
        if security_policy_name is not None:
            input_["security_policy_name"] = security_policy_name
        input_["server_id"] = server_id
        if workflow_details is not None:
            input_["workflow_details"] = workflow_details
        if structured_log_destinations is not None:
            input_["structured_log_destinations"] = structured_log_destinations
        if s3_storage_options is not None:
            input_["s3_storage_options"] = s3_storage_options
        if ip_address_type is not None:
            input_["ip_address_type"] = ip_address_type
        if identity_provider_type is not None:
            input_["identity_provider_type"] = identity_provider_type

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def delete(
        self,
        server_id: "aws_sdk_transfer.types.server_id.ServerId",
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
    ) -> None:
        """<p>Deletes the file transfer protocol-enabled server that you specify.</p> <p>No response returns from this operation.</p>

        Args:
            server_id: <p>A unique system-assigned identifier for a server instance.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.delete_server_request.DeleteServerRequest]",
        ) -> AsyncOperationResponse[None]:
            import aws_sdk_transfer._operations.transfer_service.delete_server

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.delete_server.async_delete_server(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.delete_server_request.DeleteServerRequest = {}  # type: ignore[typeddict-item]
        input_["server_id"] = server_id

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output

    async def list(
        self,
        *,
        config_overrides: Optional[AsyncTransferClientConfig] = None,
        max_results: Optional["aws_sdk_transfer.types.max_results.MaxResults"] = None,
        next_token: Optional["aws_sdk_transfer.types.next_token.NextToken"] = None,
    ) -> "aws_sdk_transfer.types.list_servers_response.ListServersResponse":
        """<p>Lists the file transfer protocol-enabled servers that are associated with your Amazon Web Services account.</p>

        Args:
            max_results: <p>Specifies the number of servers to return as a response to the <code>ListServers</code> query.</p>
            next_token: <p>When additional results are obtained from the <code>ListServers</code> command, a <code>NextToken</code> parameter is returned in the output. You can then pass the <code>NextToken</code> parameter in a subsequent command to continue listing additional servers.</p>
        """

        async def _handler(
            req: "AsyncOperationRequest[aws_sdk_transfer.types.list_servers_request.ListServersRequest]",
        ) -> AsyncOperationResponse[
            "aws_sdk_transfer.types.list_servers_response.ListServersResponse"
        ]:
            import aws_sdk_transfer._operations.transfer_service.list_servers

            (
                output,
                http_response,
            ) = await aws_sdk_transfer._operations.transfer_service.list_servers.async_list_servers(
                req.options, req.input
            )
            return AsyncOperationResponse(output=output, response=http_response)

        interceptors_, options_ = self._service.operation_options(config_overrides)
        input_: aws_sdk_transfer.types.list_servers_request.ListServersRequest = {}  # type: ignore[typeddict-item]
        if max_results is not None:
            input_["max_results"] = max_results
        if next_token is not None:
            input_["next_token"] = next_token

        response = await aexecute_pipeline(
            AsyncOperationRequest(input=input_, options=options_),
            handler=_handler,
            interceptors=list(interceptors_),
        )
        return response.output
